from lib2to3.pytree import Node

from requests import post
from toml import TomlPreserveCommentDecoder


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

    def add(self, key, value = None):
        node = TreeNode(key, value)
        if self.root == None:
            self.root = node
            return

        current = self.root

        while current:
            if current.key > key:
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
     
    def find(self, key):
    
        if self.root == None:
            return None

        node = self.root

        while node != None:
            if (node.key == key):
                return node.value
            if node.key < key:
                node = node.right
            else:
                node = node.left




    # Time Complexity: 
    # Space Complexity: 

    def inorder_helper_norecursion(self, current_node, trav_list):
        #Initialize a holding place
        stack = []

        # Loop until all the nodes are visited
        while current_node or stack:
            # If current node ,then push it in the stack and assign current to left node
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            # If current is none, pop the value and append it to the node visited 
            else:
                current_node = stack.pop()
                trav_list.append({'key':current_node.key, 'value':current_node.value})
                # Now get the right node
                current_node = current_node.right
        return trav_list        

    def inorder_helper(self, current_node, trav_list):
        if current_node == None:
            return
        if current_node.left:
            trav_list = self.inorder_helper(current_node.left, trav_list)
        # visit root node
        trav_list.append({'key':current_node.key, 'value':current_node.value})
        # visit right Tree
        if current_node.right:
            trav_list = self.inorder_helper(current_node.right, trav_list)
        return trav_list

    def inorder(self):
        trav_list = []
        #now call the helper to append to this array away from the fray of traversal
        self.inorder_helper(self.root, trav_list)
        return trav_list

    # Time Complexity: 
    # Space Complexity:     

    def preorder_helper(self, current_node, trav_list):
        if current_node == None:
            return []
        # visit root node
        trav_list.append({'key':current_node.key, 'value':current_node.value})

        # visit right Tree
        if current_node.left:
            trav_list = self.preorder_helper(current_node.left, trav_list)

        if current_node.right:
            trav_list = self.preorder_helper(current_node.right, trav_list)

        return trav_list
    
    def preorder(self):
        trav_list = []
        self.preorder_helper(self.root, trav_list)
        return trav_list


    # Time Complexity: 
    # Space Complexity:
    def postorder_helper(self, current_node, trav_list):
        if current_node == None:
            return []

        # visit right Tree
        if current_node.left:
            trav_list = self.postorder_helper(current_node.left, trav_list)

        if current_node.right:
            trav_list = self.postorder_helper(current_node.right, trav_list)

        # visit root node
        trav_list.append({'key':current_node.key, 'value':current_node.value})


        return trav_list


    def postorder(self):
        trav_list = []
        self.postorder_helper(self.root, trav_list)
        return trav_list

    # Time Complexity: 
    # Space Complexity:     
    def height_helper(self, current_node):
        if current_node is not None:
            height_left = self.height_helper(current_node.left)
            height_right = self.height_helper(current_node.right)
            return (max(height_left, height_right)+1)
        else:
            return 0

    def height (self):
        return self.height_helper(self.root)

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
