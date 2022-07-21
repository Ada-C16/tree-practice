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

    # Time Complexity: O(log n) if the tree is balanced
    # Space Complexity: O(1) - we are just creating one object (the new node)
    
    def add_helper(self, current_root, new_node):
        #we can treat each sub-tree like it's a new tree
        if current_root is None:
            return new_node
        
        if new_node.key < current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)
        else:
            current_root.right = self.add_helper(current_root.right, new_node)

        return current_root


    def add(self, key, value = None):
        new_node = TreeNode(key, value) #creating the node we are going to add
        if self.root == None:
            self.root = new_node
            return self.root 

        current = self.root 
        while current:
            if current.key > key: 
                #go left
                if current.left is None: #I am at the bottom
                    #so add the node
                    current.left = new_node
                else:
                    current = current.left
            else:
                #go right
                if current.right is None:
                    current.right = new_node
                else:
                    current = current.right
        #Since there is a root,
        #Checking whether the new value is bigger than the root
        else:
            if value < self.root.value:
                self.root.left = self.add(self.root.left, value)
            else:
                self.root.right = self.add(self.root.right, value)

            return self.root


    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        #check if there's anything in the tree
        if self.root == None:
            return None
        
        if self.root.key == key:
            return self.root.value
        
        current = self.root
        while current:
            if current.key > key:
                #go left
                if current.left is None:
                    #we are at the bottom.. nothing else here
                    print("Not sure what to do here")
            else:
                if current.right is None:
                    break



        
        

    # Time Complexity: 
    # Space Complexity: 

    #lets you take the tree and get back an array w all the elements sorted in order
    def inorder_helper(self, current_node, items):
        
        if current_node is not None:
            self.inorder_helper(current_node.left, items)
            items.append({"key": current_node.key, "value": current_node.value})
            self.inorder(current_node.right, items)
        
        

        



    def inorder(self):
        pass

        # items = []
        # self.inorder_helper(self.root, items)

        # return items


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
