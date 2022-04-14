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

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if not self.root:
            self.root = new_node
            return
        self.add_helper(self.root, new_node)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def find(self, key):
        if not self.root:
            return None
        result = self.find_helper(self.root, key)
        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def inorder(self):
        items = []
        self.inorder_helper(self.root, items)
        return items

    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)
        return items

    # Time Complexity: O(n)
    # Space Complexity: O(n)     
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)
        return items

    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def height(self):
        if not self.root:
            return 0
        height = 0
        height += self.height_helper(self.root, height)
        return height


#  Optional Method
# Time Complexity: O(n)
# Space Complexity: O(n) 
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
    
    #Helper functions:


    def add_helper(self, cur_root, new_node):
        if cur_root is None:
            return new_node

        if new_node.key < cur_root.key:
            cur_root.left = self.add_helper(cur_root.left, new_node)
        else:
            cur_root.right = self.add_helper(cur_root.right, new_node)
        return cur_root
    
    
    def find_helper(self, cur_root, key):
        if cur_root:
            if key == cur_root.key:
                return cur_root.value
 
            if key > cur_root.key:
                cur_root = cur_root.right
                result = self.find_helper(cur_root, key)

            elif key < cur_root.key:
                cur_root = cur_root.left
                result = self.find_helper(cur_root, key)
            return result
        
        
    def inorder_helper(self, cur, items):
        if cur is not None:
            self.inorder_helper(cur.left, items)
            items.append({"key": cur.key, "value": cur.value})
            self.inorder_helper(cur.right, items)
        
        
    def preorder_helper(self, cur, items):
        if cur is not None:
            items.append({"key": cur.key, "value": cur.value})
            if cur.left is not None:
                self.preorder_helper(cur.left, items)
            if cur.right is not None:
                self.preorder_helper(cur.right, items)
                
                
    def postorder_helper(self, cur, items):
        if cur is not None:
            self.postorder_helper(cur.left, items)
            self.postorder_helper(cur.right, items)
            items.append({"key": cur.key, "value": cur.value})
            
            
    def height_helper(self, cur, height):
        if cur:   
            if not cur.left and not cur.right:
                return 1
            else:
                left = self.height_helper(cur.left, height) + 1
                right = self.height_helper(cur.right, height) + 1

                if left > right:
                    height += left
                else:
                    height += right
        return height
    
    def bfs_helper(self, items):
        for node in items:
            if node.left is not None:
                items.append(node.left)
            if node.right is not None:
                items.append(node.right)