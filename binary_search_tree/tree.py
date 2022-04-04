from multiprocessing.pool import IMapUnorderedIterator


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

    def add_helper(self, current_node, new_node):
        if new_node.key <= current_node.key:
            if current_node.left:
                return self.add_helper(current_node.left, new_node)
            else:
                current_node.left = new_node
                return
        else:
            if current_node.right:
                return self.add_helper(current_node.right, new_node)
            else:
                current_node.right = new_node
                return

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if self.root == None:
            self.root = new_node
        else:
            self.add_helper(self.root, new_node)

    def find_helper(self, node, key):
        if node == None:
            return None
        if node.key == key:
            return node.value
        if key < node.key:
            return self.find_helper(node.left, key)
        else:
            return self.find_helper(node.right, key)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        return self.find_helper(self.root, key)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder_helper(self, node, arr):
        if node == None:
            return
        self.inorder_helper(node.left, arr)
        arr.append({"key": node.key, "value": node.value})
        self.inorder_helper(node.right, arr)

    def inorder(self):
        arr = []

        self.inorder_helper(self.root, arr)
        return arr

    def preorder_helper(self, node, arr):
        if node == None:
            return
        
        arr.append({"key": node.key, "value": node.value})
        self.preorder_helper(node.left, arr)
        self.preorder_helper(node.right, arr)

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder(self):
        arr = []

        self.preorder_helper(self.root, arr)
        return arr

    def postorder_helper(self, node, arr):
        if node == None:
            return
        
        self.postorder_helper(node.left, arr)
        self.postorder_helper(node.right, arr)
        arr.append({"key": node.key, "value": node.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        arr = []
        self.postorder_helper(self.root, arr)
        return arr

    def height_helper(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.height_helper(node.left), self.height_helper(node.right))

    # Time Complexity: O(n)
    # Space Complexity: O(1)  
    def height(self):
        return self.height_helper(self.root)

#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        # create a 'q'
        # add the root to it
        # while there is something in the q
        # dequeue and add its children
        # when we dequeue, add the values to the 'expected answer' array
        vals = []
        if not self.root:
            return vals

        q = [self.root]
        while q:
            curr = q.pop(0)
            vals.append({"key": curr.key, "value": curr.value})
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return vals



        
        


        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
