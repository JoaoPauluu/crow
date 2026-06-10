import { useEffect, useState } from "react";
import Node from "../models/Node";

interface NodeInterfaceProps {
    nodeId?: string;
}


function NodeInterface({ nodeId }: NodeInterfaceProps) {
    if (!nodeId) { return <div><h1>No node selected</h1></div> }

    const [node, setNode] = useState<Node | null>(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const fetchNode = async () => {
          setIsLoading(true);
            try {
                const response = await fetch(`http://localhost:8000/node/${nodeId}`);
                const data = await response.json();
                setNode(new Node(data));
            } catch (error) {
                console.error("Error fetching node:", error);
            } finally {
                setIsLoading(false);
            }
        };
        
        console.log(node);

        fetchNode();
    }, [nodeId])


    return (
      <>
        {isLoading ? <h1>Loading...</h1>
        : <div>
            <h1>Node loaded</h1>
            <p>{node?.to_string()}</p>
          </div>}
      </>
    );
}

export default NodeInterface;