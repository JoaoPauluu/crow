import ListGroup from "./ListGroup";
import useNodes from "../hooks/useNodes";


interface NodeListProps {
    setSelectedNode: (id: string) => void;
}


function NodeList({ setSelectedNode }: NodeListProps) {
    const { isPending, error, data: nodes } = useNodes()
    if (isPending) {
        return <h1>Loading nodes...</h1>
    }
    if (error) {
        return <h1>Something went wrong when loading the nodes: {error.message}</h1>
    }

    const reduced_nodes = nodes.map((node) => {
        return {id: node.id, name: node.header.name, OnClick() {setSelectedNode(node.id)}}
    })


    return (
        <div>
            <ListGroup items={reduced_nodes} listName="Nodes"/>
        </div>
    )
}

export default NodeList;