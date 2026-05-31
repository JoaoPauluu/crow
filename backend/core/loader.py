#from core.project import Project
from core.data_nodes import Node
from typing import Optional
from pathlib import Path



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
    
    
