interface NodeHeader {
    name: string;
    tags: string[];
    type: string;
}

interface NodeContent {
    baseContent: any[];
    specificContent: any[];
}

interface NodeMeta {
    author: string;
    created_at: string;
    updated_at: string;
}

interface NodeConnections {
    parents: string[];
    children: string[];
    siblings: string[];
}

interface NodeData {
    id: string;
    header: NodeHeader;
    content: NodeContent;
    meta: NodeMeta;
    connections: NodeConnections;
}

interface ShortNodeData {
    id:string;
    header: NodeHeader;
    connections:NodeConnections
}

export type { NodeHeader, NodeContent, NodeMeta, NodeData, NodeConnections, ShortNodeData};