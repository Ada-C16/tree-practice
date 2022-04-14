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

    # Time Complexity: worst case O(N)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if not self.root:
            self.root = new_node
            return
        curr = self.root
        while curr:
            if key < curr.key:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    return
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    return

    # Time Complexity: worst case O(N)
    # Space Complexity: 0(1)
    def find(self, key):
        result = self.get_node(key, self.root)
        if result:
            return result.value
        return None

    def get_node(self, key, node):
        if not node:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self.get_node(key, node.left)
        return self.get_node(key, node.right)

    # Time Complexity: worst case O(N)
    # Space Complexity: O(n)
    def inorder(self):
        if self.root == None:
            return []
        arr = []
        self.inorder_helper(self.root, arr)
        return arr
    
    def inorder_helper(self, node, arr):
        if node is not None:
            self.inorder_helper(node.left, arr)
            arr.append(self.node_info(node))
            self.inorder_helper(node.right, arr)

    # Time Complexity: worst case O(N)
    # Space Complexity: O(n)
    def preorder(self):
        if self.root == None:
            return []
        arr = []
        self.preorder_helper(self.root, arr)
        return arr
    
    def preorder_helper(self, node, arr):
        if node:
            arr.append(self.node_info(node))
            self.preorder_helper(node.left, arr)
            self.preorder_helper(node.right, arr)

    # Time Complexity: worst case O(N)
    # Space Complexity: O(n)
    def postorder(self):
        if self.root == None:
            return []
        arr = []
        self.postorder_helper(self.root, arr)
        return arr
    
    def postorder_helper(self, node, arr):
        if node:
            self.postorder_helper(node.left, arr)
            self.postorder_helper(node.right, arr)
            arr.append(self.node_info(node))

    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, node):
        if not node:
            return 0
        return 1 + max(self.height_helper(node.left), self.height_helper(node.right))

    def node_info(self, node):
        return {
            "key": node.key,
            "value": node.value,
            }

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"