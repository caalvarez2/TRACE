import asyncio
import json
import pprint
from Crawler import crawl_site  
from treestructuremanager import TreeStructureManager  

async def main():
    # Define a sample website for testing.
    sample_url = "http://example.com"  # Use a small, simple website for testing.
    print("Starting crawl on:", sample_url)
    
    # Run the crawler with a shallow depth (e.g., depth=1 for testing).
    crawled_data = await crawl_site(sample_url, depth=1)
    print("\nCrawling complete. Crawled data:")
    pprint.pprint(crawled_data, width=120)
    
    # Initialize the TreeStructureManager.
    manager = TreeStructureManager()
    manager.initialize()  # Optional if __init__ already creates an empty structure.
    
    # Feed each crawled URL into the tree structure manager.
    for record in crawled_data:
        url = record.get('url')
        if url:
            manager.add_url(url)
    
    # Convert the nested dictionary into a UI-friendly tree node format.
    tree_nodes = manager.get_tree_nodes()
    print("\nFormatted Tree JSON:")
    print(json.dumps(tree_nodes, indent=2))

if __name__ == '__main__':
    asyncio.run(main())
