import { useQuery } from '@tanstack/react-query'    
import { type ShortNodeData } from '../types/Node';


async function  fetchNodes() {
            try {
                const response = await fetch("http://localhost:8000/nodes");
                if (!response.ok) {
                    throw Error("Response was not ok!")
                }
                return response.json();
            } catch (error: unknown) {
                console.error("Error fetching nodes: ", error);
                throw error
            } 
}


export default function useNodes() {
    const query = useQuery<ShortNodeData[]>({
        queryKey: ['nodes'],
        queryFn: fetchNodes
    })

    return query
}