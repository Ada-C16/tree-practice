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

    def add_helper(self, current_node, new_node):
        if current_node is None:
            return new_node

        elif new_node.key < current_node.key:
            current_node.left = self.add_helper(current_node.left, new_node)
        else:
            current_node.right = self.add_helper(current_node.right, new_node)
        return current_node

    # Time Complexity: O(log n)
    # Space Complexity: O(1) 
    def add(self, key, value = None):
        new_node = TreeNode(key, value)

        if self.root is None:
            self.root = new_node
            return self.root
        self.add_helper(self.root, new_node)

    def find_helper(self, current_node, key):
        if current_node == None:
            return None
        elif current_node.key == key:
            return current_node.value
        elif current_node.key > key:
            return self.find_helper(current_node.left, key)
        else:
            return self.find_helper(current_node.right, key)

    # Time Complexity: O(log n)
    # Space Complexity: O(1) 
    def find(self, key):
        if self.root == None:
            return None

        return self.find_helper(self.root, key)
        

    def inorder_helper(self, current_node, items):
        if current_node is not None:
            self.inorder_helper(current_node.left, items)
            items.append({"key": current_node.key, "value":current_node.value})
            self.inorder_helper(current_node.right, items)

    # Time Complexity:O(n) 
    # Space Complexity: O(n)
    def inorder(self):
        items = []

        self.inorder_helper(self.root, items)
        return items

    def preorder_helper(self, current_node, items):
        if current_node is not None:
            items.append({"key": current_node.key, "value":current_node.value})
            self.preorder_helper(current_node.left, items)
            self.preorder_helper(current_node.right, items)
        

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)
        return items


    def postorder_helper(self, current_node, items):
        if current_node is not None:
            self.postorder_helper(current_node.left, items)
            self.postorder_helper(current_node.right, items)
            items.append({"key":current_node.key, "value": current_node.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)
        return items

    # Time Complexity:O(n) 
    # Space Complexity: O(n) 

    def height_helper(self, current_node):
        if current_node is None:
            return 0
        left_height = self.height_helper(current_node.left)
        right_height = self.height_helper(current_node.right)
        return max(left_height, right_height) + 1


    def height(self):
        if self.root is None:
            return -1
            
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: O(n^2)
#   # Space Complexity: O(n)
    def bfs(self):
        def bfs_helper(queue, arr):
            if queue == [] or queue[0] is None:
                return arr
            current = queue.pop(0)
            arr.append({"key":current.key, "value":current.value})
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            return bfs_helper(queue, arr)
        return bfs_helper([self.root], [])

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
