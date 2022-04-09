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

    def add_helper(self, current_root, new_node):

        if current_root is None:
            return new_node
        
        if new_node.key < current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)
        elif new_node.key > current_root.key:
            current_root.right = self.add_helper(current_root.right, new_node)

        return current_root


    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)

        if not self.root:
            self.root = new_node
            return
        
        self.add_helper(self.root, new_node)


    def find_helper(self, current_root, key):

        if current_root:

            if key == current_root.key:
                return current_root.value

            if key > current_root.key:
                current_root = current_root.right
                result = self.find_helper(current_root, key)
            
            elif key < current_root.key:
                current_root = current_root.left
                result = self.find_helper(current_root, key)
            return result

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def find(self, key): 
        if not self.root:
            return None

        result = self.find_helper(self.root, key)

        return result


    def inorder_helper(self, current, items):
        if current is not None:
            self.inorder_helper(current.left, items)
            items.append({"key": current.key, "value": current.value})
            self.inorder_helper(current.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []
        self.inorder_helper(self.root, items)

        return items
    
    def preorder_helper(self, current, items):
        if current is not None:
            items.append({"key": current.key, "value": current.value})

            if current.left is not None:
                self.preorder_helper(current.left, items)

            if current.right is not None:
                self.preorder_helper(current.right, items)
        
        

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)
        return items

    def postorder_helper(self, current, items):
        if current is not None:
            self.postorder_helper(current.left, items)
            self.postorder_helper(current.right, items)
            items.append({"key": current.key, "value": current.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)
        print(items)
        return items

    def height_helper(self, current, height):

        if current:

            if not current.left and not current.right:
                return 1
            
            else:
                left = self.height_helper(current.left, height) + 1
                right = self.height_helper(current.right, height) + 1

                if left > right:
                    height += left
                else:
                    height += right
        
        return height

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def height(self):

        if not self.root:
            return 0
        
        height = 0

        height += self.height_helper(self.root, height)
        
        return height

    def bfs_helper(self, items):

        for node in items:
            if node.left is not None:
                items.append(node.left)
            
            if node.right is not None:
                items.append(node.right)


#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        items = []
        if not self.root:
            return items
        
        items.append(self.root)

        self.bfs_helper(items)

        result = []

        for node in items:
            result.append({'key': node.key, 'value': node.value})

        return result

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
