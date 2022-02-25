from unittest.mock import NonCallableMagicMock


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
    # Space Complexity: O(1)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
            return self.root
        else:
            return self.add_helper(self.root, key, value)
        
    def add_helper(self, cur, key, value):
        if cur == None:
            return TreeNode(key, value)
        else:
            if key < cur.key:
                cur.left = self.add_helper(cur.left, key, value)
                return cur
            else:
                cur.right = self.add_helper(cur.right, key, value)
                return cur

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        else:
            return self.find_recursive(self.root, key)
    
    def find_recursive (self, cur, key):
        if cur == None:
            return None
        elif cur.key == key:
            return cur.value
        else: # cur.key != key
            if key < cur.key:
                return self.find_recursive(cur.left, key)
            else:
                return self.find_recursive(cur.right, key)

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        pass

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


tree = Tree()
print(tree.root == None)
tree.add(5, "Peter")
tree.add(7, "Ada")
tree.add(10)
tree.add(3)
tree.add(4)


print(tree.root.key == 5)
print(tree.root.right.key == 7)
print(tree.root.right.right.key == 10)
print(tree.root.left.key == 3)
print(tree.root.left.right.key == 4)