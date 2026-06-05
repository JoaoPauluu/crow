from core.data_nodes_types import NodeType
from core.data_nodes import Node
from core.loader import Loader
from typing import Optional


class Project:
    def __init__(self, directory:str):
        self.directory: str = directory
        self.node_types: list[NodeType] = Loader.load_default_node_types() + Loader.load_custom_node_types(self)
        self.node_types_names = [node_type.name for node_type in self.node_types]
        self.loaded_nodes: list[Node] = Loader.load_all_nodes(self.directory)

    def get_node(self, node_id: str) -> Optional['Node']:
        for node in self.loaded_nodes:
            if node.id == node_id:
                return node
        return None
    