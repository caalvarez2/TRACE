from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.post("/run-crawler")
def run_crawler():
    """
    Runs driver.py via a subprocess.
    The driver.py runs the crawler and tree structure manager,
    printing the tree graph to the backend console.
    """
    try:
        # Adjust the command if necessary (e.g., "python3" or use an absolute path)
        result = subprocess.run(
            ["python", "routers/driver.py"],
            capture_output=True,
            text=True,
            check=True
        )
        # Print the output to the backend console
        print("driver.py output:")
        print(result.stdout)
        return {"success": True, "message": "Driver executed successfully"}
    except subprocess.CalledProcessError as e:
        print("Error running driver.py:", e)
        return {"success": False, "error": str(e)}
