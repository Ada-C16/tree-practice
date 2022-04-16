class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        
# tests 1 and 5 pass without doing anything

class Tree:
    def __init__(self):
        self.root = None

    def add_helper(self, current_root, new_node):
        if current_root is None:
            return new_node
        if new_node.key < current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)
        elif new_node.key > current_root.key:
            current_root.right = self.add_helper(current_root.right, new_node)

        return current_root

    # Time Complexity: log n
    # Space Complexity: log n

    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if not self.root:
            self.root = new_node
            return
        self.add_helper(self.root, new_node)

    # Time Complexity: log n
    # Space Complexity: log n
    def find(self, key):
        current = self.root

        while current:
            if current.key == key:
                print("PRINT STATEMENT if clause", key)
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        print("PRINT STATEMENT before return none", current)
        return None

    def inorder_helper(self, current_node, items):
        if current_node is not None:
            self.inorder_helper(current_node.left, items)
            items.append({"key": current_node.key, "value": current_node.value})
            self.inorder_helper(current_node.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []
        self.inorder_helper(self.root, items)
        return items

    def preorder_helper(self, current_node, items):
        if current_node is None:
            return

        items.append({"key": current_node.key, "value": current_node.value})
        self.preorder_helper(current_node.left, items)
        self.preorder_helper(current_node.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)
        return items


    def postorder_helper(self, current_node, items):
        if current_node is None:
            return
        self.postorder_helper(current_node.left, items)
        self.postorder_helper(current_node.right, items)
        items.append({"key": current_node.key, "value": current_node.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)

        return items

    def height_helper(self, current_node):
        if current_node is not None:
            height_left = self.height_helper(current_node.left)
            height_right = self.height_helper(current_node.right)
            return max(height_left, height_right) +1
        else:
            return 0

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height(self):
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
