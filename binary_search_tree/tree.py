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

    def addHelper(self, current_root, new_node):
        if current_root is None:
            return new_node
        
        if new_node.key < current_root.key:
            if current_root.left is None:
                # current_root.left = self.addHelper(current_root.left, new_node)
                current_root.left = new_node
            else:
                self.addHelper(current_root.left, new_node)
        else:
            if current_root.right is None:
                # current_root.right = self.addHelper(current_root.right, new_node)
                current_root.right = new_node
            else:
                self.addHelper(current_root.right, new_node)

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        new_node = TreeNode(key, value)

        if self.root is None:
            self.root = new_node
            return 
        self.addHelper(self.root, new_node)

    
    def findHelper(self, current_node, key):
        if not current_node:
            print('in first case')
            return None
        if current_node.key == key:
            print('in found case')
            return current_node.value
        if current_node.key > key:
            print('in left case')
            return self.findHelper(current_node.left, key)
        if current_node.key < key:
            print('in right case')
            return self.findHelper(current_node.right, key)    

    # Time Complexity: 
    # Space Complexity:
    def find(self, key):
        #if it's empty return None
        return self.findHelper(self.root, key)

    def inorderHelper(self, current, result):
        if current:
            self.inorderHelper(current.left, result)
            result.append({"key": current.key, "value": current.value})
            self.inorderHelper(current.right, result)

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        #only instantiate once
        result = []
        self.inorderHelper(self.root, result)
        return result


    # Time Complexity: 
    # Space Complexity: 
    def preorderHelper(self, current, result):
        if current:
            result.append({"key": current.key, "value": current.value})
            self.preorderHelper(current.left, result)
            self.preorderHelper(current.right, result)


    def preorder(self):
        result = []
        self.preorderHelper(self.root, result)
        return result

    def postorderHelper(self, current, result):
        if current:
            self.postorderHelper(current.left, result)
            self.postorderHelper(current.right, result)
            result.append({"key": current.key, "value": current.value})

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        result = []
        self.postorderHelper(self.root, result)
        return result

    def heightHelper(self, current):
        if current is None:
            return 0
        else:
            left = self.heightHelper(current.left)
            right = self.heightHelper(current.right)
            
            if left > right:
                return left + 1
            else:
                return right + 1
    
    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        current = self.root
        if current is None:
            return 0 
        return self.heightHelper(current)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"


# class Driver:
#     my_tree = Tree()

#     my_tree.add(5, "Peter")
#     my_tree.add(3, "Paul")
#     my_tree.add(1, "Mary")
#     my_tree.add(10, "Karla")
#     my_tree.add(15, "Ada")
#     my_tree.add(25, "Kari")

#     my_tree.find(1) == "Mary"
#     # my_tree.find(25) == "Kari"
#     # my_tree.add(13, "Alicia")
#     # my_tree.find(13) == "Alicia"


    #def inorder(self):
        # result = []
        # if self.root.left:
        #     result += self.root.left.inorder()

        # result.append(self.root.value)

        # if self.root.right:
        #     result += self.root.right.inorder()

        # return result