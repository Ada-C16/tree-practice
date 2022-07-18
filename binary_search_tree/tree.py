from queue import Queue


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

    # Time Complexity: O(log(n))
    # Space Complexity: O(1) 
    def add(self, key, value = None):
        def add_helper(node, key, value = None):
            if key < node.key:
                if node.left is None:
                    node.left = TreeNode(key, value)
                    return
                else:
                    add_helper(node.left, key, value)
                    return
            if key > node.key:
                if node.right is None:
                    node.right = TreeNode(key, value)
                    return
                else:
                    add_helper(node.right, key, value)
                    return

        if self.root is None:
            self.root = TreeNode(key, value)
            return
        add_helper(self.root, key, value)

    # Time Complexity: O(log(n)) 
    # Space Complexity: O(log(n)) 
    def find(self, key):
        def find_helper(node, key):
            if node is None:
                return None
            elif node.key == key:
                return node.value
            elif key < node.key:
                return find_helper(node.left, key)
            elif key > node.key:
                return find_helper(node.right, key)

        return find_helper(self.root, key)

    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    def inorder(self):
        def inorder_helper(inorder_list, node):
            if node is None:
                return
            inorder_helper(inorder_list, node.left)
            inorder_list.append({"key": node.key, "value": node.value})
            inorder_helper(inorder_list, node.right)

        inorder_list = []
        inorder_helper(inorder_list, self.root)
        return inorder_list

    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    def preorder(self):
        def preorder_helper(inorder_list, node):
            if node is None:
                return
            preorder_list.append({"key": node.key, "value": node.value})
            preorder_helper(inorder_list, node.left)
            preorder_helper(inorder_list, node.right)

        preorder_list = []
        preorder_helper(preorder_list, self.root)
        return preorder_list

    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    def postorder(self):
        def postorder_helper(inorder_list, node):
            if node is None:
                return
            postorder_helper(inorder_list, node.left)
            postorder_helper(inorder_list, node.right)
            postorder_list.append({"key": node.key, "value": node.value})

        postorder_list = []
        postorder_helper(postorder_list, self.root)
        return postorder_list

    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    def height(self):
        def height_helper(node):
            if node is None:
                return 0
            return 1 + max(height_helper(node.left), height_helper(node.right))
        return height_helper(self.root) 


#   # Optional Method
    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    def bfs(self):
        if self.root is None:
            return []


        bfs_result = []
        bfs_queue = Queue()
        bfs_queue.put(self.root)
        while not bfs_queue.empty():
            node = bfs_queue.get()
            bfs_result.append({"key": node.key, "value": node.value})
            if node.left is not None:
                bfs_queue.put(node.left)
            if node.right is not None:
                bfs_queue.put(node.right)

        return bfs_result

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
