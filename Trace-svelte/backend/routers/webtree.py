from fastapi import APIRouter
from models import TreeNode

router = APIRouter()

# Stub: In-memory tree structure
tree_data = TreeNode(
    id=1,
    name="Root",
    children=[
        TreeNode(id=2, name="Child 1", children=[]),
        TreeNode(id=3, name="Child 2", children=[
            TreeNode(id=4, name="Grandchild 1", children=[])
        ])
    ]
)

@router.get("/", response_model=TreeNode)
async def get_tree():
    # Stub: In a real application, query the database or processing output.
    return tree_data
