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

    def add_helper(self, current_node, key, value ):
        if current_node == None:
            return TreeNode(key, value)
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node 

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value) 
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        if self.root == None:
            return None
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif  current.key >= key: 
                current = current.left
            else:
                current = current.right
        return None

    # In-Order: Left, Current, Right
    def inorder_helper(self, root, inorder_list):
        if root:
        # Traverse left
            self.inorder_helper(root.left, inorder_list)
        # Traverse root
            # print(str(root.val) + "->", end='')
            inorder_list.append({"key" : root.key, "value" : root.value})
        # Traverse right
            self.inorder_helper(root.right, inorder_list)
        return inorder_list

    # # Time Complexity: 
    # # Space Complexity: 
    def inorder(self):
        inorder_list = []
        if self.root == None:
            return inorder_list
        else:
            return self.inorder_helper(self.root, inorder_list)

    def preorder_helper(self, root, preorder_list):
        if root:
            preorder_list.append({"key" : root.key, "value" : root.value})
            self.preorder_helper(root.left, preorder_list)
            self.preorder_helper(root.right, preorder_list)
        return preorder_list

    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        preorder_list = []
        if self.root == None:
            return preorder_list
        else:
            return self.preorder_helper(self.root, preorder_list)

    def postorder_helper(self, root, postorder_list):
        if root:
            self.postorder_helper(root.left, postorder_list)
            self.postorder_helper(root.right, postorder_list)
            postorder_list.append({"key" : root.key, "value" : root.value})
        return postorder_list

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        postorder_list = []
        if self.root == None:
            return postorder_list
        else:
            return self.postorder_helper(self.root, postorder_list)


    def height_helper(self, root):
        if root == None:
            return 0
        lefth= self.height_helper(root.left)
        righth = self.height_helper(root.right)

        if lefth > righth:
            return lefth + 1
        else:
            return righth + 1

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        if self.root == None:
            return 0
        else:
            return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
