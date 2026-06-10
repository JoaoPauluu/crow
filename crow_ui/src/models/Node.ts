import { type NodeHeader,  type NodeContent, type NodeMeta, type NodeData, type NodeConnections } from "../types/Node";

class Node implements NodeData {
    id: string;
    header: NodeHeader;
    content: NodeContent;
    meta: NodeMeta;
    connections: NodeConnections;

    constructor({id, header, content, meta, connections}: NodeData) {
        this.id = id;
        this.header = header;
        this.content = content;
        this.meta = meta;
        this.connections = connections;
    }

    to_string() {
        return `Node ${this.id}: ${this.header.name}`;
    }
}

export default Node;
