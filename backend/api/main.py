from core.data_nodes import Node
from core.project import Project
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AppState:
    project: Project | None = None

state = AppState()

#for testing purposes only, remove later
state.project = Project(directory="S:/crow_project_example")


@app.get("/")
def read_root():
    return {"Hello": "World"}

class LoadProjectRequest(BaseModel):
    project_directory: str

@app.post("/action/load_project")
def load_project(request: LoadProjectRequest):
    if state.project is not None:
        return {"error": "A project is already loaded. Please unload it first."}
    state.project = Project(directory=request.project_directory)
    return {"message": "Project loaded successfully"}

@app.post("/action/unload_project")
def unload_project():
    state.project = None
    return {"message": "Project unloaded successfully"}


@app.get("/node")
def get_all_nodes():
    if state.project is None:
        return {"error": "No project loaded"}

    nodes = state.project.loaded_nodes
    return {"nodes": [{"node_id": node.id, "node_header": node.header, "node_content": node.content} for node in nodes]}

@app.get("/node/{node_id}")
def get_node(node_id: str):
    if state.project is None:
        return {"error": "No project loaded"}

    node = state.project.get_node(node_id)
    if node is None:
        return {"error": "Node not found"}

    return {"node_id": node.id, "node_header": node.header, "node_content": node.content}