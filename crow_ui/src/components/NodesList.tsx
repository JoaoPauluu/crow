import ListGroup from "./ListGroup";
import { useState, useEffect, type MouseEvent } from "react";


interface NodeListProps {
    setSelectedNode: (id: string) => void;
}

interface Node {
    id: string;
    header: {
        name: string;
    };
}

function NodeList({ setSelectedNode }: NodeListProps) {
    const [nodes, setNodes] = useState<Node[]>([]);

    useEffect(() => {
        const fetchNodes = async () => {
            try {
                const response = await fetch("http://localhost:8000/nodes");
                const data = await response.json();
                setNodes(data);
            } catch (error) {
                console.error("Error fetching nodes:", error);
            }
        };

        fetchNodes();
    }, [])

    const reduced_nodes = nodes.map((node) => {
        return {id: node.id, name: node.header.name, OnClick(event: MouseEvent) {setSelectedNode(node.id)}}
    })


    return (
        <div>
            <ListGroup items={reduced_nodes} listName="Nodes"/>
        </div>
    )
}

export default NodeList;