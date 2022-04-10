"""
Given the root of a binary search tree, 
rearrange the tree in in-order so that the leftmost node in the 
tree is now the root of the tree, and every node has no 
left child and only one right child.


Input: root node
Output: root node

inorder df tree traversal


   4
  / \
3     5

1. find lowest val, make it root

2. Add all other nodes in order
store parent
parent.left = current.right
current.right = parent

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root
        self.cur = None

    def inorder(self, node):
        if node:
            self.inorder(node.left)

            node.left = None
            self.cur.right = node
            self.cur = node

            self.inorder(node.right)

    def increasingBST(self, root):
        new_tree = self.cur = TreeNode()
        self.inorder(root)
        return new_tree.right
