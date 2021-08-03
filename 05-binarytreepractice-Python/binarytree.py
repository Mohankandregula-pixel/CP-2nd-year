class Node(object):
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def _init_(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """
        Return True if the find_val is in the tree and False otherwise.
        """
        # Your code goes here
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
        # Your code goes here
        return self.preorder_print(self.root, "")[:-1]

    def preorder_search(self, start, find_val):
        """
        Helper method - use this to create a recursive search solution.
        """
        # Your code goes here
        return start.value == find_val or self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val) if start else False

    def preorder_print(self, start, traversal):
        """
        Helper method - use this to create a recursive print solution.
        """
        # Your code goes here
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal