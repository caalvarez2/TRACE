# state.py
from routers.treestructuremanager import TreeStructureManager

# Global variables to store state
tree_data = []
tree_manager = None

def init_tree_manager():
    global tree_manager
    if tree_manager is None:
        tree_manager = TreeStructureManager()
        tree_manager.initialize()
    return tree_manager

def update_tree_data():
    global tree_data, tree_manager
    if tree_manager is not None:
        tree_data.clear()
        tree_data.extend(tree_manager.get_tree_nodes())
    return tree_data