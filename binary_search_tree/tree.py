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
        cur = self.root
        if cur == None:
            self.root = TreeNode(key, value)
            return
        while True:
            if key < cur.key:
                if cur.left == None:
                    cur.left = TreeNode(key, value)
                    return
                else:
                    cur = cur.left
            else:
                if cur.right == None:
                    cur.right = TreeNode(key, value)
                    return
                else:
                    cur = cur.right
            


    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        cur = self.root
        if cur == None:
            return None
        while cur != None and cur.key != key:
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        if cur == None:
            return None
        return cur.value

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        result = []
        def inorder_helper(node):
            if node == None:
                return
            if node.left != None:
                inorder_helper(node.left)
            result.append({
                "key": node.key,
                "value": node.value
            })
            if node.right != None:
                inorder_helper(node.right)
        inorder_helper(self.root)
        return result
                

        

        

    # Time Complexity: O(n)
    # Space Complexity:  O(n)  
    def preorder(self):
        result = []
        def preorder_helper(node):
            if node == None:
                return
            result.append({
                "key": node.key,
                "value": node.value
            })
            if node.left != None:
                preorder_helper(node.left)
            if node.right != None:
                preorder_helper(node.right)
        preorder_helper(self.root)
        return result

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        result = []
        def postorder_helper(node):
            if node == None:
                return
            if node.left != None:
                postorder_helper(node.left)
            if node.right != None:
                postorder_helper(node.right)
            result.append({
                "key": node.key,
                "value": node.value
            })
        postorder_helper(self.root)
        return result
    
    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        if self.root == None:
            return 0
        def height_helper(node, height):
            if node == None:
                return
            left_best = -1
            right_best = -1
            if node.left != None:
                left_best = height_helper(node.left, height + 1)
            if node.right != None:
                right_best = height_helper(node.right, height + 1)
            return max([left_best, right_best, height])
        return height_helper(self.root, 1)

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        cur = self.root
        if cur == None:
            return []
        
        res = [{
            "key": self.root.key,
            "value": self.root.value
        }]
        parents = [self.root]

        while len(parents) > 0:
            new_parents = []
            for parent in parents:
                if parent.left != None:
                    res.append({
                        "key": parent.left.key,
                        "value": parent.left.value
                    })
                    new_parents.append(parent.left)
                if parent.right != None:
                    res.append({
                        "key": parent.right.key,
                        "value": parent.right.value

                    })
                    new_parents.append(parent.right)
            parents = new_parents
        return res

        

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
