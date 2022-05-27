from turtle import right


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

    # Time Complexity: O(1)
    # Space Complexity: O(N)
    def add_helper(self,node,key,value):
        if node is None:
            return TreeNode(key,value)
        if key < node.key:
            node.left = self.add_helper(node.left, key, value)
        else:
            node.right = self.add_helper(node.right, key, value)

        return node


    def add(self, key, value = None):
        self.root = self.add_helper(self.root,key,value)

        



    # Time Complexity: O(N)
    # Space Complexity: O(1) - no additional databases
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


    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def inorder(self):
        array_of_nodes = []
        def inorder_helper(root):
            if root is not None:
                inorder_helper(root.left)
                array_of_nodes.append({"key": root.key,"value": root.value})
                inorder_helper(root.right)
        inorder_helper(self.root)
        return array_of_nodes

            


        

    # Time Complexity: O(N)
    # Space Complexity: O(N)    
    def preorder(self):
        array_of_nodes = []
        def preorder_helper(root):
            if root is not None:
                array_of_nodes.append({"key": root.key,"value": root.value})
                preorder_helper(root.left)
                preorder_helper(root.right)
        preorder_helper(self.root)
        return array_of_nodes



    # Time Complexity: O(N)
    # Space Complexity:O(N)
    def postorder(self):
        array_of_nodes = []
        def postorder_helper(root):
            if root is not None:
                postorder_helper(root.left)
                postorder_helper(root.right)
                array_of_nodes.append({"key": root.key,"value": root.value})
        postorder_helper(self.root)
        return array_of_nodes

    # Time Complexity: O(1)
    # Space Complexity:O(1)  
    def height(self):
        def height_helper(root):
            if root is None:
                return 0
            else:
                left_height = height_helper(root.left)
                right_height = height_helper(root.right)
                return max(left_height, right_height) + 1
        return height_helper(self.root)



#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
