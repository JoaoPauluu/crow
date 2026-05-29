from data_nodes import Node
from loader import Loader
from typing import Optional


class Project:
    def __init__(self, directory:str):
        self.directory: str = directory
        self.loaded_nodes: list[Node] = Loader.load_all_nodes(self.directory)

    def get_node(self, node_id: str) -> Optional['Node']:
        for node in self.loaded_nodes:
            if node.id == node_id:
                return node
        return None
    