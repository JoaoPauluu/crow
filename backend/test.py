from platform import node

from core.data_nodes import Node
from core.project import Project

def main():
    ##node = Node.from_crw_file("S:/crow_project_example/node_example.crw")
    node_dict = {
        "header": {
            "name": "lemma topzera cu 2",
            "type": "example",
            "tags": ["cálculo", "integração"]
        },
        "content": {
            "base_content": ["comentário teste"],
            "specific_content": ["enunciado do teorema", "prova do teorema"]
        },
        "connections": {
            "parents": [],
            "children": [],
            "lateral": []
        },
        "meta": {
            "author": "João Paulo"
        }
    }

    node = Node.new_node_from_dict(node_dict)
    project = Project(directory="S:/crow_project_example")
    node.save(project.directory)
    #print(project.loaded_nodes)
    print(node)
    #print(project.loaded_nodes)


if __name__ == "__main__":
    main()