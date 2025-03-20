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

@router.post("/run-crawler")
def run_crawler():
    """
    Runs driver.py in a subprocess. Returns stdout/stderr in JSON format.
    """
    try:
        # Adjust command/path if needed (e.g., "python3" vs. "python").
        # Also ensure 'driver.py' is in the same directory or provide a full path.
        result = subprocess.run(
            ["python", "driver.py"], 
            capture_output=True, 
            text=True, 
            check=True
        )
        return {
            "success": True,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.CalledProcessError as e:
        # If driver.py fails (non-zero exit code), capture details
        return {
            "success": False,
            "error": str(e),
            "stdout": e.stdout,
            "stderr": e.stderr
        }