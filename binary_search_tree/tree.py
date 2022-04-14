from xml.etree.ElementPath import find


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

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):        
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            new_node = TreeNode(key, value)
            current = self.root
            if new_node.key < current.key:
                if not current.left:
                    current.left = new_node 
                    return
                elif not current.right:
                    current.right = new_node 
                    return            


    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        current = self.root

        while current:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None                 

    def inorder_helper(self, current, values):
        if not current:
            return values

        self.inorder_helper(current.left, values)
        values.append({
            "key": current.key,
            "value": current.value
        })

        self.inorder_helper(current.right, values)
        return values

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        values = [] 
        return self.inorder_helper(self.root, values)


    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        pass

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        pass

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        pass


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
