from logging import root
from multiprocessing.sharedctypes import Value
from unittest import result


class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        


class Tree:
    def __init__(self):
        self.root = None

    def add_helper(self,current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)
        if key < current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def find(self, key):
        if self.root == None:
            return None
        
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left
        return None


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        if self.root == None:
            return []
        arr = []
        self.inorder_helper(self.root, arr)
        return arr

    def inorder_helper(self, node, arr):
        if node is not None:
            self.inorder_helper(node.left, arr)
            arr.append({"key": node.key, "value": node.value})
            self.inorder_helper(node.right, arr)


    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def preorder(self):
        result = []
        def preorder_helper(current_node):
            if current_node == None:
                return result
            result.append({"key": current_node.key, "value": current_node.value})
            preorder_helper(current_node.left)
            preorder_helper(current_node.right)
        preorder_helper(self.root)
        return result


    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def postorder(self):
        result = []
        def postorder_helper(current_node):
            if current_node == None:
                return result
            postorder_helper(current_node.left)
            postorder_helper(current_node.right)
            result.append({"key": current_node.key, "value": current_node.value})
        postorder_helper(self.root)
        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def height(self):
        def height_helper(current_node):
            if current_node == None:
                return 0
            left_height = height_helper(current_node.left)
            right_height = height_helper(current_node.right)
            return max(left_height, right_height) + 1
        return height_helper(self.root)


# Optional Method
# Time Complexity: 
# Space Complexity: 
    # def bfs(self):
    #     result = []
    #     queue = []
    #     queue.append(self.root)
    #     while len(queue) > 0:
    #         current = queue.pop(0)
    #         result.append(current.key)
    #         if current.left != None:
    #             queue.append(current.left)
    #         if current.right != None:
    #             queue.append(current.right)
    #     return result

        
# *********notes from the video*********
# if you have a very unbalanced tree, the time complexity is going to be O(n)
# if you have a balanced tree, the time complexity is going to be O(log n). much better.
# red-black tree is a balanced tree. 
# a traversal is when you visit every node in a tree.
# depth first traversals are: pre-order, in-order, post-order
# pre-order: visit the root, then the left subtree, then the right subtree. if you need to save a tree data structure to disk, of sent it across the network and maintain the structure, pre-order traversals can be useful.
# in-order: visit the left subtree, then the root, then the right subtree. if you need to sort a list, in-order traversals are useful.
# post-order: visit the left subtree, then the right subtree, then the root. if you need to delete a node from a tree, post-order traversals are useful.
# binary search tree is an ordered data structure in which the every node in the left subtree is "less" than or equal to the current nocde and every node in the right subtree is greater than the current node.
# a balanced binary search tree provides O(log n) time complexity for adding, removing and finding values in the tree.
# an unbalanced tree more resenbles a linked list in time complexity for find and arbitraty insertions and deletions O(n)
# a traversal is an algorithm which visits every node in a tree.
# examples include: breadth first search, inorder, postorder, preorder. 
# ****************************************

