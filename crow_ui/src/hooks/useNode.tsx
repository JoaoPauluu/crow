import { useQuery } from '@tanstack/react-query'
import { type NodeData } from '../types/Node'

async function fetchNode(nodeId:string) {
    try {
        const response = await fetch(`http://localhost:8000/node/${nodeId}`);
        if (!response.ok) {
            throw Error("Response not okay!")
        }
        return response.json();
    } catch (error: unknown) {
        console.error("Error fetching node:", error);
        throw error
    }
}

export default function useNode(nodeId:string) {
    const query = useQuery<NodeData>({
        queryKey: ['node', nodeId],
        queryFn: async () => {return fetchNode(nodeId)}
    })

    return query
}
