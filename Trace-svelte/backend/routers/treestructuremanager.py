class TreeStructureManager:
    def __init__(self):
        # Contract: @ensures(self.tree_structure is not None)
        self.tree_structure = {}
    
    def initialize(self):
        """
        @requires(Crawler.has_executed_successfully() and DirectoryBruteForcer.has_executed_successfully())
        @ensures(self.tree_structure is not None)
        Initializes an empty tree structure.
        """
        self.tree_structure = {}

    def add_directory(self, path: str):
        """
        @requires(path is not None and isinstance(path, str))
        @ensures(path in self.tree_structure) 
        Adds a directory to the tree based on the provided path.
        """
        if not path or not isinstance(path, str):
            raise ValueError("Path must be a non-empty string")

        parts = path.strip("/").split("/")
        current = self.tree_structure
        for part in parts:
            if part not in current:
                # Each directory is represented by a dictionary
                current[part] = {}
            current = current[part]

    def add_file(self, path: str, filename: str):
        """
        @requires(path is not None and filename is not None and isinstance(path, str) and isinstance(filename, str))
        @ensures(filename in self.tree_structure[path])
        Adds a file under the specified directory node.
        """
        if not path or not filename:
            raise ValueError("Both path and filename must be provided and be strings.")

        parts = path.strip("/").split("/")
        current = self.tree_structure
        for part in parts:
            if part not in current:
                raise KeyError(f"Directory '{part}' does not exist. Please add the directory first.")
            current = current[part]
        # Represent a file as a key with a None value (or you could use a special marker)
        current[filename] = None

    def get_structure(self) -> dict:
        """
        @requires(self.tree_structure is not None)
        @ensures(return instanceof Dictionary)
        Returns the current hierarchical structure as a nested dictionary.
        """
        return self.tree_structure

    def remove_node(self, path: str):
        """
        @requires(path in self.tree_structure)
        @ensures(path not in self.tree_structure)
        Removes a node (directory or file) from the tree.
        """
        if not path or not isinstance(path, str):
            raise ValueError("Path must be a non-empty string")
        
        parts = path.strip("/").split("/")
        if not parts:
            return
        
        # Helper recursive function to remove the node.
        def _remove(current: dict, parts: list) -> bool:
            # If we're at the last part, remove it.
            if len(parts) == 1:
                if parts[0] in current:
                    del current[parts[0]]
                    return True
                return False
            # Otherwise, continue traversing
            head = parts[0]
            if head not in current or not isinstance(current[head], dict):
                return False
            removed = _remove(current[head], parts[1:])
            # Optionally clean up an empty directory
            if removed and not current[head]:
                del current[head]
            return removed

        removed = _remove(self.tree_structure, parts)
        if not removed:
            raise KeyError(f"Path '{path}' not found in the tree structure.")

# Example usage:
if __name__ == '__main__':
    manager = TreeStructureManager()
    manager.initialize()
    # Add some directories and files
    manager.add_directory("root/subdir1")
    manager.add_directory("root/subdir2")
    manager.add_file("root/subdir1", "file1.txt")
    manager.add_file("root/subdir1", "file2.txt")
    manager.add_file("root/subdir2", "image.png")

    print("Tree structure:")
    import pprint
    pprint.pprint(manager.get_structure())

    # Remove a file
    manager.remove_node("root/subdir1/file1.txt")
    print("\nAfter removal:")
    pprint.pprint(manager.get_structure())
