
class TreeNode:
    def __init__(self, value, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

    def __repr__(self):
        return str(self.value)

class BST:
    def __init__(self, root_node):
        self.root_node = root_node

    def find_parent_node__(self, value, node):
        if (node.leftChild and node.leftChild.value == value) or (node.rightChild and node.rightChild.value == value):
            return node
        else:
            if node.value > value:
                return self.find_parent_node__(value, node=node.leftChild)
            elif node.value < value:
                return self.find_parent_node__(value, node=node.rightChild)

    def search(self, value, node):
        # 2 base case:
        if node is None:
            return node
        if node.value == value:
            return node

        # recurse:
        if value < node.value:
            return self.search(value, node.leftChild)
        elif value > node.value:
            return self.search(value, node.rightChild)

    def insert(self, value, node):
        if value < node.value:
            if node.leftChild is None:
                node.leftChild = TreeNode(value)
                return
            self.insert(value, node.leftChild)
        else:
            if node.rightChild is None:
                node.rightChild = TreeNode(value)
                return
            self.insert(value, node.rightChild)

    def find_successor_node__(self, node):
        if node.leftChild is None:
            return node
        return self.find_successor_node__(node.leftChild)

    def delete(self, value):
        node = self.search(value, node=self.root_node)
        parent = self.find_parent_node__(node.value, node=self.root_node)

        # ------------ if node has 0 child, delete it
        if node.leftChild is None and node.rightChild is None:
            if node.value < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return

        # ------------ if node has 1 child only
        # - case where it's only 1 left child
        elif node.leftChild is not None and node.rightChild is None:
            parent.rightChild = node.leftChild
            return
        # - case where it's only 1 right child
        elif node.leftChild is None and node.rightChild is not None:
            parent.leftChild = node.rightChild
            return

        # ------------ if node has 2 children
        # step 1: find successor node
        move_one_right = node.rightChild
        successor_node = self.find_successor_node__(move_one_right)

        # step 2: delete that successor node:
        parent_successor = self.find_parent_node__(successor_node.value, node=self.root_node)
        if successor_node.value < parent_successor.value:
            # remove left child
            parent_successor.leftChild = None
        else:
            # remove right child
            parent_successor.rightChild = None

        # step 3: replace node with successor node
        node.value = successor_node.value

        # step 4: (optional), if the
        # successor node has a right child
        if successor_node.rightChild:
            parent_successor.leftChild = successor_node.rightChild

    def traverse(self, node):
        if node is None:
            return 'plop'
        self.traverse(node.leftChild)
        print(node.value)
        self.traverse(node.rightChild)


# build a clean tree
node_8 = TreeNode(62, None, None)

node_7 = TreeNode(89, None, None)
node_6 = TreeNode(56, None, rightChild=node_8)

node_5 = TreeNode(33, None, None)
node_4 = TreeNode(10, None, None)

node_3 = TreeNode(75, node_6, node_7)
node_2 = TreeNode(25, node_4, node_5)

root_node = TreeNode(50, leftChild=node_2, rightChild=node_3)

myBST = BST(root_node=root_node)


# test the operations:

# searching
assert myBST.search(899, node=root_node) is None
assert myBST.search(89, node=root_node).value == 89
assert myBST.search(50, node=root_node).value == 50

# inserting
myBST.insert(10000, node=root_node)
# 10000 is inserted at the extreme bottom right of the tree:
assert myBST.search(89, node=root_node).__dict__['rightChild'].value == 10000

# traversing
myBST.insert(1, node=root_node)
myBST.traverse(root_node)
# out= 1, 10, 25, 33, 50, 56, 62, 75, 89, 10000

# deleting
myBST.delete(10000)
myBST.traverse(root_node)
# out= 1, 10, 25, 33, 50, 56, 62, 75, 89

assert myBST.search(89, node=root_node).__dict__['rightChild'] == None