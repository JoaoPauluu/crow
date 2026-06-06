import ListGroup from "./ListGroup";
import { useState, useEffect } from "react";


interface NodeListProps {
    setSelectedNode: (id: string) => void;
}

function NodeList({ setSelectedNode }: NodeListProps) {
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

    const [nodes, setNodes] = useState([]);
    const reduced_nodes = nodes.map((node) => {
        return {id: node.id, name: node.name, OnClick() {setSelectedNode(node.id)}}
    })


    return (
        <div>
            <ListGroup items={reduced_nodes} listName="Nodes"/>
        </div>
    )
}

export default NodeList;