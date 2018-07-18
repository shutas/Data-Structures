"""Class implementations for BNode and BTree."""

# Written by Shuta Suzuki (shutas@umich.edu)

class BNode:
    """BNode class that are the building blocks for BTree"""
    def __init__(self, label_str, parent_node=None):
        """Initializer for BNode."""
        self.label = label_str
        self.parent = parent_node
        self.children = []


    def __repr__(self):
        """For printing."""
        return self.label


class BTree:
    """BTree is the collection of connected BNodes"""
    def __init__(self, root_node):
        if root_node.parent:
            raise Exception("Initial BNode cannot have a parent node")
        self.root = root_node

    
    def __repr__(self):
        """For printing."""
        return "BTree with root node: " + str(self.root)


    def _insert(self, new_node, current_node):
        """Helper function to insert BNode to BTree. DFS."""
        if current_node == new_node.parent:
            current_node.children.append(new_node)
            new_node.parent = current_node
            return
        if current_node.children:
            for child in current_node.children:
                self._insert(new_node, child)


    def insert(self, new_node):
        """Insert BNode to tree. Print error if node cannot be inserted."""
        self._insert(new_node, self.root)