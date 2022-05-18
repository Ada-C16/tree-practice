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
        if self.root == None:
            self.root = TreeNode(key, value)
            return
            
        def add_helper(current):
            if key < current.key:
                if current.left is not None:
                    add_helper(current.left)
                else:
                    current.left = TreeNode(key, value)
            else:
                if current.right is not None:
                    add_helper(current.right)
                else:
                    current.right = TreeNode(key,value)
        
        add_helper(self.root)

    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        if self.root == None:
            return None

        def find_helper(current):
            if current.key == key:
                return current.value
            elif key < current.key:
                if current.left is not None:
                    return find_helper(current.left)
            else:
                if current.right is not None:
                    return find_helper(current.right)
        return find_helper(self.root)

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        return_list = []
        current = self.root
        if self.root == None:
            return return_list

        def in_order_helper(current):
            if current.left is not None:
                in_order_helper(current.left)
            return_list.append({'key': current.key, 'value': current.value})
            if current.right is not None:
                in_order_helper(current.right)
        
        in_order_helper(current)
        return return_list

    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        return_list = []
        current = self.root
        if self.root == None:
            return return_list

        def pre_order_helper(current):
            return_list.append({'key': current.key, 'value': current.value})
            if current.left is not None:
                pre_order_helper(current.left)
            if current.right is not None:
                pre_order_helper(current.right)
        
        pre_order_helper(current)
        return return_list

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        return_list = []
        current = self.root
        if self.root == None:
            return return_list

        def post_order_helper(current):
            if current.left is not None:
                post_order_helper(current.left)
            if current.right is not None:
                post_order_helper(current.right)
            return_list.append({'key': current.key, 'value': current.value})
        
        post_order_helper(current)
        return return_list

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        #check for greatest number
        #+1 going down stack, -1 going up stack
        heights = 1
        max_height = 0
        current = self.root
        if self.root == None:
            return 0

        def height_helper(current):
            nonlocal heights
            nonlocal max_height
            if heights > max_height:
                max_height = heights
            if current.left is not None:
                heights +=1
                height_helper(current.left)
            if current.right is not None:
                heights +=1
                height_helper(current.right)
            heights-=1
        
        height_helper(current)
        return max_height


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
