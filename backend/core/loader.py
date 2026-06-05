from core.data_nodes import Node
from core.data_nodes_types import NodeType
from typing import TYPE_CHECKING
from pathlib import Path

if TYPE_CHECKING:
    from core.project import Project


class Loader:
    @classmethod
    def load_node(cls, file_path: str) -> 'Node':
        return Node.from_crw_file(file_path)
    
    @classmethod
    def load_all_nodes(cls, directory: str) -> list['Node']:
        nodes = []
        errors = []

        for crw_file in Path(directory).rglob("*.crw"):
            try:
                node = cls.load_node(str(crw_file))
                nodes.append(node)
            except Exception as e:
                errors.append((str(crw_file), e))

        if errors:
            for path, error in errors:
                print(f"[Loader] Failed to load {path}: {error}")

        return nodes
    
    @classmethod
    def load_node_type(cls, file_path: str) -> 'NodeType':
        return NodeType.from_json_file(file_path)
    
    @classmethod
    def load_default_node_types(cls) -> list['NodeType']:
        default_nodes_dir = Path(__file__).parent / "default_nodes"
        return [cls.load_node_type(str(file)) for file in Path(default_nodes_dir).rglob("*.json")]
    
    @classmethod
    def load_custom_node_types(cls, project: 'Project') -> list['NodeType']:
        custom_nodes_dir = Path(project.directory) / "custom_nodes"
        if not custom_nodes_dir.exists():
            return []
        return [cls.load_node_type(str(file)) for file in custom_nodes_dir.rglob("*.json")]