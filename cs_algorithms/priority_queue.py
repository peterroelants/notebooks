class BinaryHeap():
    """
    Binary Heap datastructure.
    Each node is larger than or equal to the keys in that node's two children (if any).
    The largest key is found at the root.

    The parent of the node at index i can be found at index floor(i/2).
    The 2 children of a node at index i can be found at index 2i and 2i+1

    The heap is indexed by the algorithm starting from index 1.
    """
    def __init__(self):
        # Set the heap
        self.heap = [None]

    def size(self):
        return len(self.heap)-1

    def swim(self, i):
        """
        Bottom-up reheapify (swim).
        Fix heap violation when a node's key becomes LARGER than that node's PARENT key.
        """
        # Keep exchanging the parent at floor(i/2) if this parent is smaller than the current child at i,
        # and while i is still in the range of the heap list
        while i > 1 and self.heap[i//2] < self.heap[i]:
            # Exchange parent with child if parent < child
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            # Update position in heap
            i //= 2

    def sink(self, i):
        """
        Top-down reheapify (sink).
        Fix heap violation when a node's key becomes SMALLER than than one or both of that
        node's CHILDREN's keys.
        """
        # Keep exchanging the larger child at 2i or 2i+1 (j) with the current parent at i,
        # while the child index is still withing the heap, and the parent is still smaller than the child.
        while 2*i <= self.size():
            # Get the child at position j=2i
            j = 2*i
            if j < self.size() and self.heap[j] < self.heap[j+1]:
                # Set j to j+1 if the child at j+1 is larger than the child at j.
                # The child that needs to be exchanged with the parent needs to be
                # larger than the other child.
                j += 1
            if not self.heap[i] < self.heap[j]:
                # Stop if the parent at i is larger or equal to the child at j
                break
            # Exchange parent with larger child
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            # Update i to the child because we need to check the new child at j
            # in the next iteration.
            i = j

    def insert(self, key):
        """
        Insert the given key into the heap.
        """
        # Insert the key at the end of the list
        self.heap.append(key)
        # Fix the possible heap violation
        self.swim(self.size())

    def max(self):
        """
        Return the maximum element in the heap
        """
        # The maximum element is at index 1. (index 0 is not used)
        return self.heap[1]

    def delete_max(self):
        """
        Delete and return the maximal element in the heap
        """
        max = self.max()
        n = self.size()
        # Exchange the maximum with the last elemnt in the heap
        self.heap[1], self.heap[n] = self.heap[n], self.heap[1]
        # Remove the last (maximum now) element
        self.heap.pop()
        # Fix the heap violation
        self.sink(1)
        return max

    def is_empty(self):
        """
        Return true if and only if this heap is empty.
        """
        return self.size() == 0
