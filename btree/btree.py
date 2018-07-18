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
        # If new_node is a child of current_node, add new_node
        if current_node == new_node.parent:
            current_node.children.append(new_node)
            new_node.parent = current_node
            return "Inserted"

        # Check if any child nodes are parent of new_node
        elif current_node.children:
            for child in current_node.children:
                result = self._insert(new_node, child)
                if result:
                    return "Found"

        # Insert failed at this stage
        return None


    def insert(self, new_node):
        """Insert BNode to tree. Print error if node cannot be inserted."""
        # Insert BNode
        inserted = self._insert(new_node, self.root)

        # BNode cannot be inserted
        if not inserted:
            print("Error: BNode not inserted")

    
    def _locate(self, label_str, current_node):
        """Helper function to locate BNode in BTree. DFS."""
        # If curr_node has label_str, print parents' labels until root
        if current_node.label == label_str:
            while current_node != self.root:
                print current_node.label + " >> ",
                current_node = current_node.parent
            print self.root.label
            return "Found"

        # Check if any child nodes have the label_str as its label
        elif current_node.children:
            for child in current_node.children:
                result = self._locate(label_str, child)
                if result:
                    return "Found"

        # Locate failed at this stage
        return None

    def locate(self, label_str):
        """Locate label """
        # Locate BNode
        located = self._locate(label_str, self.root)
        
        # BNode not found
        if not located:
            print "Error: BNode not found"