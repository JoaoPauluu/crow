//import ListGroup from "./components/ListGroup";
import NodeInterface from "./components/NodeInterface";
import NodesList from "./components/NodesList";
import { type MouseEvent , useState} from "react";

function App() {
  //const items_list_2 = [{ id: 1, name: "test4" }, { id: 2, name: "test5" }, { id: 3, name: "test6" }];
  const [selectedNode, setSelectedNode] = useState<string>("");

  return (
    <div>
      <NodesList setSelectedNode={setSelectedNode} />
      <NodeInterface nodeId={selectedNode} />
    </div>
  )
}

export default App;