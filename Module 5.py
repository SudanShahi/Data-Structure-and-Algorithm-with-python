#1
class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST
        """
        current_node = self._root_node
        parent_node = None

        # Traverse tree to find insert position
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        # Insert node
        if parent_node is None:
            self._root_node = new_node
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Returns:
        - Node if found
        - None if not found
        """
        current_node = self._root_node

        while current_node:
            if data == current_node.data:
                return current_node
            elif data < current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        return None


# -------- TEST --------
if __name__ == "__main__":
    t = Tree()

    t.insert(35)
    t.insert(20)
    t.insert(40)

    print(t._find(35))   # expected: 35<><>#
    print(t._find(20))
    print(t._find(99))   # expected: None


#2
class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        current_node = self._root_node
        parent_node = None

        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        if parent_node is None:
            if self._root_node is None:
                self._root_node = new_node
            else:
                raise(ValueError)
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def find_minimum(self):
        """
        Returns the node with the minimum value
        """
        current = self._root_node
        if current is None:
            return None

        while current._left_child:
            current = current._left_child

        return current

    def find_maximum(self):
        """
        Returns the node with the maximum value
        """
        current = self._root_node
        if current is None:
            return None

        while current._right_child:
            current = current._right_child

        return current



#3class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST
        """
        current_node = self._root_node
        parent_node = None

        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        if parent_node is None:
            if self._root_node is None:
                self._root_node = new_node
            else:
                raise(ValueError)

        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.
        """
        current = self._root_node

        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child

        return None

    def _detach_node(self, node):
        """
        Detach a node from the tree.
        Node must have at most one child.
        Raises ValueError if the node has two children.
        """

        if node is None:
            return

        # Node with two children cannot be detached
        if node._left_child is not None and node._right_child is not None:
            raise ValueError

        parent = node._parent

        # Determine child (if any)
        if node._left_child is not None:
            child = node._left_child
        else:
            child = node._right_child

        # Case 1: node is root
        if parent is None:
            self._root_node = child
            if child is not None:
                child._parent = None

        # Case 2: node is left child of parent
        elif parent._left_child == node:
            parent._left_child = child
            if child is not None:
                child._parent = parent

        # Case 3: node is right child of parent
        else:
            parent._right_child = child
            if child is not None:
                child._parent = parent

        # Fully detach node
        node._parent = None
        node._left_child = None
        node._right_child = None
