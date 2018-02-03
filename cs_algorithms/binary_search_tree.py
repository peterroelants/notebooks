class Node(object):
    """
    Class to represent a node in a binary search tree
    """
    def __init__(self, key, left=None, right=None):
        """
        Initialise the node
        """
        self.left = left
        self.right = right
        self.key = key

    def get(self, get_key):
        """
        Get the node with the given key. Return None if not found.
        """
        if self.key == get_key:
            return self.key
        elif self.key < get_key and not self.right is None:
                return self.right.get(get_key)
        elif self.key > get_key and not self.left is None:
            return self.left.get(get_key)
        else:
            return None

    def put(self, new_key):
        """
        Put the given key in the BST starting at this node.
        """
        if self.key < new_key:
            if self.right is None:
                self.right = Node(new_key)
            else:
                self.right.put(new_key)
        elif self.key > new_key:
            if self.left is None:
                self.left = Node(new_key)
            else:
                self.left.put(new_key)

    def min(self):
        """
        Return the minimum in the BST under this node
        """
        if self.left is None:
            return self.key
        else:
            return self.left.min()

    def max(self):
        """
        Return the maximum in the BST under this node
        """
        if self.right is None:
            return self.key
        else:
            return self.right.max()

    def __str__(self):
        """
        Represent the node as a string.
        """
        s ='{'
        if not self.left is None:
            s += str(self.left)
        s += str(self.key)
        if not self.right is None:
            s += str(self.right)
        s += '}'
        return s


class BST(object):
    """
    Class to represent a binary search tree
    """
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.root.get(key)

    def put(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root.put(key)

    def min(self):
        if self.root is None:
            return None
        return self.root.min()

    def max(self):
        if self.root is None:
            return None
        return self.root.max()

    def delete_min(self):
        # replace the root with the root with the minimum removed
        self.root = BST.delete_min_rec(self.root)

    @staticmethod
    def delete_min_rec(node):
        # If the current left node is empty, the current node is the minimum
        # return the right of the current node to replace the current node in the previous call.
        if node.left is None:
            return node.right
        # The current left node should be the left node with the minimum deleted
        node.left = BST.delete_min_rec(node.left)
        # Return the current node to replace the current node with the minimum removed
        return node

    def delete(self, key):
        # The tree with the key element removed is the same tree with the element removed
        self.root = BST.delete_rec(self.root, key)

    @staticmethod
    def delete_rec(n, key):
        if n is None:
            return None
        if key < n.key:
            # If the deleted key is on the left, replace the left part of the tree
            # with the left part were key is deleted.
            n.left = BST.delete_rec(n.left, key)
        elif key > n.key:
            # If the deleted key is on the right, replace the right part of the tree
            # with the right part were key is deleted.
            n.right = BST.delete_rec(n.right, key)
        else:  # key == n.key
            # Remove the key at this position
            if n.right is None:
                # If the right is empty, just replace the current node with its left part
                return n.left
            if n.left is None:
                # If the left is empty, just replace the current node with its right part
                return n.right
            # Left or right is not empty
            # all nodes from n.left < key, all nodes from n.right > key
            # so new key needs to be the minimum key from n.right to keep this property true.
            # Create new node as minimum of t.right (minimum has never any left nodes)
            new_n = Node(n.right.min())
            # Remove this minimum from n.right and set the result as the right of the new node
            new_n.right = BST.delete_min_rec(n.right)
            # set the left node of the current node (minimum of right, minimum has no left nodes)
            new_n.left = n.left
            n = new_n
        return n

    def __str__(self):
        """
        Represent the tree as a string.
        """
        return str(self.root)