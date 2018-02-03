class Node(object):
    """
    Class to represent a node in a binary search tree
    """
    def __init__(self, key, left=None, right=None, is_red=False):
        """
        Initialise the node
        """
        self.left = left
        self.right = right
        self.key = key
        self.is_red = is_red

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


class RedBlackTree(object):
    """
    Class to represent a binary search tree
    """
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.root.get(key)

    def put(self, key):
        self.root =RedBlackTree.put_rec(self.root, key)
        self.root.is_red = False

    @staticmethod
    def put_rec(n, key):
        if n is None:
            # If the current node to insert the key is None return a new red Node
            # to be inserted on the parent
            return Node(key, is_red=True)
        if key < n.key:
            # Key is smaller and needs to be inserted on the left
            # The new left subtree is the current left side with the new key added
            n.left = RedBlackTree.put_rec(n.left, key)
        elif key > n.key:
            # Key is larger and needs to be inserted on the right
            # The new right subtree is the current right side with the new key added
            n.right = RedBlackTree.put_rec(n.right, key)
        # Perform rotations
        if RedBlackTree.is_red(n.right) and not RedBlackTree.is_red(n.left):
            # If the right link is red, and the left link is black:
            # rotate the red link to the left and reset the current node as the rotated link.
            n = RedBlackTree.rotate_left(n)
        if RedBlackTree.is_red(n.left) and RedBlackTree.is_red(n.left.left):
            # If the left tree contains to following red links:
            # rotate right so that the middle node become the top node.
            n = RedBlackTree.rotate_right(n)
        if RedBlackTree.is_red(n.left) and RedBlackTree.is_red(n.right):
            # Flip colors if both left and right links are red.
            RedBlackTree.flip_colors(n)
        # return the updated node
        return n

    @staticmethod
    def is_red(n):
        if n is None:
            return False
        return n.is_red

    @staticmethod
    def rotate_left(n):
        """
        Right red link of node n needs to be rotated to the left.
        """
        # get the node to the right that has the red color
        r = n.right
        if not r.is_red:
            raise ValueError('Red link expected on the right during rotate_left')
        # Put the left side of r (right side of n) on the right side of n
        # Move the left side of r through the red link to n
        n.right = r.left
        # The left side of r becomes n, r is tilted above n
        r.left = n
        # r will take the color of n
        r.is_red = n.is_red
        # n become red, the color of r
        n.is_red = True
        # return r as the new node that should be linked to the parent of n
        return r

    @staticmethod
    def rotate_right(n):
        """
        Left red link of node n needs to be rotated to the right.
        """
        # get the node to the lef that has the red color
        l = n.left
        if not l.is_red:
            raise ValueError('Red link expected on the left during rotate_right')
        # Put the right side of l (left side of n) on the left side of n
        # Move the right side of l through the red link to n
        n.left = l.right
        # The right side of l becomes n, l is tilted above n
        l.right = n
        # l will take the color of n
        l.is_red = n.is_red
        # n become red, the color of l
        l.is_red = True
        # return l as the new node that should be linked to the parent of n
        return l

    @staticmethod
    def flip_colors(n):
        """
        Flip colors of children to black, and color if this node to red
        """
        n.is_red = True
        n.left.is_red = False
        n.right.is_red = False

    def min(self):
        if self.root is None:
            return None
        return self.root.min()

    def max(self):
        if self.root is None:
            return None
        return self.root.max()

    def __str__(self):
        """
        Represent the tree as a string.
        """
        return str(self.root)