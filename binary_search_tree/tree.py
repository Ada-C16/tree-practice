# from recursive_helpers import *

class TreeNode:
    def __init__(self, key, val=None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: 
    # Space Complexity:
    # iterative approach
    def add(self, key, value=None):
        node = TreeNode(key, value)
        if self.root is None:
            self.root = node
            return
        current = self.root

        while current:
            if current.key > key:
                # ##go left
                if current.left is None:
                    # ##Add node to the left
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                # ##go right
                if current.right is None:
                    # ##Add the node on the right
                    current.right = node
                    return
                else:
                    current = current.right

    def find(self, key):
        result = self.find_helper(key, self.root)
        # catch edge case to avoid value error
        if result is not None:
            return result.value
        return result

    def find_helper(self, key, current_node):
        """

        :return:
        """
        if current_node is None or current_node.key == key:
            return current_node
        if key > current_node.key:
            return self.find_helper(key, current_node.right)
        return self.find_helper(key, current_node.left)

    # Time Complexity: 
    # Space Complexity:
    def inorder(self):
        """
        input: tree class
        :return: list of key value tuples from traversing tree inorder
        """
        inorder_result = []
        # call recursive function with current node and result_list
        self.inorder_helper(self.root, inorder_result)
        return inorder_result

    def inorder_helper(self, current_node, inorder_result):
        """
        :param current_node: self.root
        :param inorder_result: list
        :return: populates input dictionary with key and node values from BST
        """
        if current_node is None:
            return

        # traverse left side until current_node is none
        # pass in left child node and list
        self.inorder_helper(current_node.left, inorder_result)
        # append key value pairs as backtrack up the stack
        inorder_result.append({'key': current_node.key, 'value': current_node.value})
        # traverse right
        self.inorder_helper(current_node.right, inorder_result)

    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        preorder_result = []
        self.preorder_helper(self.root, preorder_result)
        return preorder_result

    def preorder_helper(self,curr_node,preorder_result):
        if curr_node is None:
            return
        preorder_result.append({'key': curr_node.key, 'value': curr_node.value})
        self.preorder_helper(curr_node.left, preorder_result)
        self.preorder_helper(curr_node.right, preorder_result)


    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        postorder_result = []
        self.postorder_helper(self.root, postorder_result)
        return postorder_result

    def postorder_helper(self,curr_node,postorder_result):
        if curr_node is None:
            return
        self.postorder_helper(curr_node.left, postorder_result)
        self.postorder_helper(curr_node.right, postorder_result)
        postorder_result.append({'key': curr_node.key, 'value': curr_node.value})


    def height_helper(self, curr_node):
        if curr_node is None:
            return 0
        return 1 + max(self.height_helper(curr_node.left), self.height_helper(curr_node.right))


    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
