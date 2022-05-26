from xml.dom import Node


class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def node_height(self):
        if self == None:
            return 0
        else:
            if self.left:
                h_left = self.left.node_height()
            else:
                h_left = 0
            if self.right:
                h_right = self.right.node_height()
            else:
                h_right = 0

            if (h_left > h_right):
                return h_left + 1
            else:
                return h_right + 1
        


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        node = TreeNode(key, value)
        if self.root is None:
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
    # Space Complexity: 0(1)
    def find(self, key):
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None


    
    # Time Complexity: O(n)
    # Space Complexity:  O(n)
    def inorder_helper(self, current, inorder_list):
        if current:
            self.inorder_helper(current.left, inorder_list)
            inorder_list.append({"key": current.key , "value":current.value})
            self.inorder_helper(current.right, inorder_list)

    def inorder(self):
        inorder_list = []
        self.inorder_helper(self.root, inorder_list)
        return inorder_list

    # Time Complexity: O(n)
    # Space Complexity:  O(n)
    def preorder_helper(self, current, preorder_list):
        if current:
            preorder_list.append({"key": current.key , "value":current.value})
            self.preorder_helper(current.left, preorder_list)
            self.preorder_helper(current.right, preorder_list)
        
    def preorder(self):
        preorder_list = []
        self.preorder_helper(self.root, preorder_list)
        return preorder_list

    # Time Complexity: O(n)
    # Space Complexity:  O(n)
    def postorder_helper(self, current, postorder_list):
        if current:
            self.postorder_helper(current.left, postorder_list)
            self.postorder_helper(current.right, postorder_list) 
            postorder_list.append({"key": current.key , "value":current.value})    
    def postorder(self):
        postorder_list = []
        self.postorder_helper(self.root, postorder_list)
        return postorder_list

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height(self):
        if self.root == None:
            return 0
        return self.root.node_height()





#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
