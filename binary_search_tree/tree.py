class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        


class Tree:
    # # ITERATIVE
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        node = TreeNode(key, value)
        if not self.root:
            self.root = node
            return self.root

        current = self.root
        previous = None
        while current:
            previous = current
            if key <= current.key:
                current = current.left
            else:
                current = current.right
        if key <= previous.key:
            previous.left = node
        else:
            previous.right = node

    # RECURSIVE
    # Time Complexity: 
    # Space Complexity: 
    # def add(self, key, value = None):
    #     # base case
    #     if not current.left and not current.right:


    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        if not self.root:
            return None
        if self.root.key == key:
            return self.root.value
        current = self.root
        while current:
            if current.key == key:
                return current.value
            if key <= current.key:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_helper(self, root, nodes):
        if root:
            self.inorder_helper(root.left, nodes)
            nodes.append({'key': root.key, 'value': root.value})
            self.inorder_helper(root.right, nodes)
        
    # Time Complexity: O(n) while n = number of nodes in BST
    # Space Complexity: O(n)
    def inorder(self):
        # left, root, right
        if not self.root:
            return []
        nodes = []

        self.inorder_helper(self.root, nodes)
        return nodes

    
    def preorder_helper(self, current, nodes):
        if current:
            nodes.append({'key': current.key, 'value': current.value})
            self.preorder_helper(current.left, nodes)
            self.preorder_helper(current.right, nodes)
        return
        
    # Time Complexity: O(n) n = number of nodes in BST
    # Space Complexity: O(n)     
    def preorder(self):
        # root -> left -> right
        if not self.root:
            return []
        nodes_list = []
        self.preorder_helper(self.root, nodes_list)
        return nodes_list


    def postorder_helper(self, current, nodes_list):
        if current:
            self.postorder_helper(current.left, nodes_list)
            self.postorder_helper(current.right, nodes_list)
            nodes_list.append({'key': current.key, 'value': current.value})

    # Time Complexity: O(n) n = number of nodes in BST
    # Space Complexity: O(n)     
    def postorder(self):
        # left -> right -> root
        if not self.root:
            return []
        nodes_list = []
        self.postorder_helper(self.root, nodes_list)
        return nodes_list


    def height_helper(self, root):
        if not root:
            return 0
        left_height = self.height_helper(root.left)
        right_height = self.height_helper(root.right)
        return 1 + max(left_height, right_height)
        

    # Time Complexity: O(n) and n = # of nodes in BST
    # Space Complexity: O(n) ? not sure on this one 
    def height(self):
        if not self.root:
            return 0
        return self.height_helper(self.root)


  # Optional Method
  # Time Complexity: O(n) where n = number of nodes in BST
  # Space Complexity: O(n)
    def bfs(self):
        if not self.root:
            return []
        queue = [ self.root ]
        values = []
        while queue:
            current = queue.pop(0)
            # {'key': 5, 'value': 'Peter'}
            values.append({'key': current.key, 'value': current.value})
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return values

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
