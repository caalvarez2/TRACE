from fastapi import APIRouter, Query
from routers.treestructuremanager import TreeStructureManager
from .state import tree_data, init_tree_manager, update_tree_data

router = APIRouter()

@router.get("/")
def get_tree(projectId: str = Query(None, description="Optional project ID to filter results")):
    # Ensure we have a tree manager initialized
    manager = init_tree_manager()
    
    # Update the global tree data to get the latest structure
    updated_data = update_tree_data()
    
    # If a project ID is specified, filter the tree data
    # This is a placeholder - you would implement actual filtering logic based on your project structure
    if projectId:
        # Simple filtering example - in reality, this would be more sophisticated
        filtered_data = [node for node in updated_data if projectId.lower() in node.get('name', '').lower()]
        return filtered_data
    
    # Otherwise return all tree data
    return updated_data

@router.post("/add-url")
def add_url(url: str = Query(..., description="URL to add to the tree structure")):
    manager = init_tree_manager()
    manager.add_url(url)
    update_tree_data()
    return {"success": True, "message": f"Added URL: {url}", "tree": tree_data}

@router.delete("/remove-node")
def remove_node(path: str = Query(..., description="Path to remove from the tree")):
    manager = init_tree_manager()
    try:
        manager.remove_node(path)
        update_tree_data()
        return {"success": True, "message": f"Removed path: {path}", "tree": tree_data}
    except KeyError as e:
        return {"success": False, "message": str(e)}
