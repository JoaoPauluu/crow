from core.data_nodes import Node
from core.project import Project

def main():
    ##node = Node.from_crw_file("S:/crow_project_example/node_example.crw")
    node_dict = {
        "header": {
            "name": "Teorema Fundamental do Cálculo",
            "type": "corollary",
            "tags": ["cálculo", "integração"]
        },
        "content": {
            "statement": "Seja f uma função contínua em [a, b] e F uma primitiva de f em [a, b]. Então: ∫[a, b] f(x) dx = F(b) - F(a).",
            "proof": "A prova do Teorema Fundamental do Cálculo é baseada na definição de integral e na propriedade das primitivas. A ideia central é mostrar que a função definida por G(x) = ∫[a, x] f(t) dt é uma primitiva de f, ou seja, G'(x) = f(x). Em seguida, usando o Teorema da Média para integrais, podemos concluir que G(b) - G(a) = ∫[a, b] f(x) dx. Como G é uma primitiva de f, temos G(b) - G(a) = F(b) - F(a), o que completa a prova."
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
    node = Node(**node_dict)
    print(node)
    project = Project(directory="S:/crow_project_example")
    node.save(project_location=project.directory)


if __name__ == "__main__":
    main()