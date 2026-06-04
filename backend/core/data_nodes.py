from datetime import datetime, timezone
from os import name
from pydantic import BaseModel, Field, model_validator
from typing import Optional, Literal, Any
from pathlib import Path
import json
import uuid

<<<<<<< HEAD
=======
#from core.project import Project
>>>>>>> 659dac7136be7f835bf9a151adc4f6c6abc9cfcf

def name_to_file_path(name: str) -> str:
    #MUST IMPLEMENT CHECKING FOR DUPLICATES TO NOT ERASE FILES!!!
    return name.lower().replace(" ", "_") + ".crw"

def get_node_types() -> list[str]:
    node_types_path = Path(__file__).parent / "NodeTypes"
    node_type_files = node_types_path.glob("*.json")
    node_types = [f.stem for f in node_type_files]  
    return node_types



class NodeHeader(BaseModel):
    name: str
    type: str
    tags: list[str] = []

class NodeContent(BaseModel):
    base_content: list[Any] = []
    specific_content: list[Any] = []

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
    
    @model_validator(mode="before")
    def validate_node_type(cls, data: dict) -> dict:
        node_type = data.get("header", {}).type
        node_types = get_node_types()
        if node_type not in node_types:
            raise ValueError(f"Invalid node type: {node_type}. Must be one of: {', '.join(node_types)}")
        return data

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

        if data.get("file_type") != "crw":
            raise ValueError(f"Not a valid .crw file: {full_file_path}")

        return cls(
            id            = data.get("id", str(uuid.uuid4())),
            relative_file_path = data.get("relative_file_path", full_file_path),
            header        = NodeHeader(**data["header"]),
            content       = NodeContent(**data["content"]),
            connections   = NodeConnections(**data.get("connections", {})),
            meta          = NodeMeta(**data.get("meta", {})),
        )
    
    @classmethod
    def new_node_from_dict(cls, data: dict) -> 'Node':
        return cls(
            id            = data.get("id", str(uuid.uuid4())),
            relative_file_path = data.get("relative_file_path", ""),
            header        = NodeHeader(**data["header"]),
            content       = NodeContent(**data["content"]),
            connections   = NodeConnections(**data.get("connections", {})),
            meta          = NodeMeta(**data.get("meta", {})),
        )