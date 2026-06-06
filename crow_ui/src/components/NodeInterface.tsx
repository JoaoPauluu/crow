interface NodeInterfaceProps {
    nodeId?: string;
}

function NodeInterface({ nodeId }: NodeInterfaceProps) {
    if (!nodeId) { return <div><h1>No node selected</h1></div> }

    return <div><h1>Node Interface for {nodeId}</h1></div>
}

export default NodeInterface;