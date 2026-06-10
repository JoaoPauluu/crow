import Node from "../models/Node";
import useNode from "../hooks/useNode";

interface NodeInterfaceProps {
    nodeId?: string;
}


function NodeInterface({ nodeId }: NodeInterfaceProps) {
    if (!nodeId) { return <div><h1>No node selected</h1></div> }

    const { isLoading, error, data:nodeData} = useNode(nodeId)
    if (isLoading) {
        return <h1>Node Loading...</h1>
    }
    if (error) {
        return <h1>Error: {error.message}</h1>
    }

    if(!nodeData) {
        throw Error("No node data!")
    }

    const node = new Node(nodeData)

    return (
      <>
         <div>
            <h1>Node loaded</h1>
            <p>{node?.to_string()}</p>
        </div>
      </>
    );
}

export default NodeInterface;