from datetime import datetime, timezone
from os import name
from pydantic import BaseModel, Field, model_validator
from typing import Optional, Literal
import json
import uuid

from project import Project

def name_to_file_path(name: str) -> str:
    return name.lower().replace(" ", "_") + ".crw"


class NodeContent(BaseModel):
    comments: str = ""

class TextContent(NodeContent):
    text: str

class DefinitionContent(NodeContent):
    statement: str

class LemmaContent(NodeContent):
    statement: str
    proof:     Optional[str] = None

class TheoremContent(NodeContent):
    statement: str
    proof:     Optional[str] = None

class CorollaryContent(NodeContent):
    statement: str
    proof:     Optional[str] = None

class ExampleContent(NodeContent):
    statement: str
    solution:  Optional[str] = None

class ExerciseContent(NodeContent):
    statement: str
    solution:  Optional[str] = None



NodeType = Literal["text", "definition", "theorem", "lemma", "corollary", "example", "exercise"]
CONTENT_MODELS: dict[str, type[NodeContent]] = {
    "text": TextContent,
    "definition": DefinitionContent,
    "theorem": TheoremContent,
    "lemma": LemmaContent,
    "corollary": CorollaryContent,
    "example": ExampleContent,
    "exercise": ExerciseContent
}


class NodeHeader(BaseModel):
    name: str
    type: NodeType
    tags: list[str] = []

class NodeConnections(BaseModel):
        parents:  list[str] = []
        children: list[str] = []
        lateral:  list[str] = []

class NodeMeta(BaseModel):
    author: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))





class Node(BaseModel):
    file_type: str = "crw"
    version: str = "1.0"
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    relative_file_path: str = ""
    header:        NodeHeader
    content:       NodeContent
    connections:   NodeConnections = NodeConnections()
    meta:          NodeMeta        = NodeMeta()
    has_been_modified: bool = False
    
    @model_validator(mode="after")
    def set_file_path(self) -> 'Node':
        if not self.relative_file_path:
            self.relative_file_path = name_to_file_path(self.header.name)
        return self

    def append_child(self, child_node: 'Node'):
        if child_node.id not in self.connections.children:
            self.connections.children.append(child_node.id)
        if self.id not in child_node.connections.parents:
            child_node.append_parent(self)

    def append_lateral(self, lateral_node: 'Node'):
        if lateral_node.id not in self.connections.lateral:
            self.connections.lateral.append(lateral_node.id)
        if self.id not in lateral_node.connections.lateral:
            lateral_node.append_lateral(self)

    def append_parent(self, parent_node: 'Node'):
        if parent_node.id not in self.connections.parents:
            self.connections.parents.append(parent_node.id)
        if self.id not in parent_node.connections.children:
            parent_node.append_child(self)



    def _full_file_path(self, project_location: str) -> str:
        return f"{project_location}/{self.relative_file_path}"

    def save(self, project_location: str, full_file_path: Optional[str] = None):
        self.meta.updated_at = datetime.now(timezone.utc)
        full_path = full_file_path or self._full_file_path(project_location)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(self.model_dump_json(indent=2))

    @classmethod
    def from_crw_file(cls, full_file_path: str) -> 'Node':
        with open(full_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if data.get("__type") != "crw":
            raise ValueError(f"Not a valid .crw file: {full_file_path}")

        node_type = data["header"]["type"]
        content_model = CONTENT_MODELS.get(node_type)
        if not content_model:
            raise ValueError(f"Unknown node type: {node_type}")

        return cls(
            id            = data.get("id", str(uuid.uuid4())),
            relative_file_path = data.get("relative_file_path", full_file_path),
            header        = NodeHeader(**data["header"]),
            content       = content_model(**data["content"]),
            connections   = NodeConnections(**data.get("connections", {})),
            meta          = NodeMeta(**data.get("meta", {})),
        )