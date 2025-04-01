from fastapi import APIRouter, HTTPException, Query
from .Crawler import crawl_site  # Ensure this is an async function
from routers.treestructuremanager import TreeStructureManager
from .state import tree_data, init_tree_manager
import asyncio


router = APIRouter()

@router.post("/run-crawler")
async def run_crawler(url: str = Query(..., description="URL to crawl"), depth: int = 1):
    try:
        crawled_data = await crawl_site(url, depth=depth)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Crawling failed: {str(e)}")
    
    manager = init_tree_manager()
    for record in crawled_data:
        record_url = record.get('url')
        if record_url:
            manager.add_url(record_url)
    
    # Update the global tree_data
    from .state import tree_data  # already imported; tree_data can be a mutable variable
    tree_data.clear()
    tree_data.extend(manager.get_tree_nodes())
    return {"success": True, "tree": tree_data}
