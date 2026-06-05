from pydantic import BaseModel, Field, model_validator
from typing import Optional, Literal, Any
import json

NodeFieldTypes = Literal["string", "file", "file", "boolean"]

class NodeField(BaseModel):
    name: str
    type: NodeFieldTypes
    description: Optional[str] = None

class NodeType(BaseModel):
    name: str
    description: Optional[str] = None
    fields: dict[str, NodeField] = {}

    @classmethod
    def from_json_file(cls, file_path: str) -> 'NodeType':
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return cls(
            name = data["name"],
            description = data.get("description"),
            fields = {field["name"]: NodeField(**field) for field in data.get("fields", [])}
        )