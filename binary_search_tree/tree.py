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

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self): # left, root, right - DFS
        """
        input: tree node - root node
        output: array 
        """
        arr = []
        if self.root == None:
            return arr
        else:
            return self.inorder_helper(self.root,arr)
        
    def inorder_helper(self, cur, arr):
        if cur == None:
            return arr
        else:
            left_arr = self.inorder_helper(cur.left, arr)
            left_arr.append({ 
                            "key" : cur.key, 
                            "value" : cur.value
                            })
            right_arr = self.inorder_helper(cur.right, left_arr)
            return right_arr

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder(self): # root, left, right
        arr = []
        if self.root == None:
            return arr
        else:
            return self.preorder_helper(self.root, arr)
    
    
    def preorder_helper(self, cur, arr):
        if cur == None:
            return arr
        else:
            cur_dict = { 
                        "key" : cur.key, 
                        "value" : cur.value
                        }
            # root
            arr.append(cur_dict)
            # left
            left_arr = self.preorder_helper(cur.left, arr)
            
            # right
            right_arr = self.preorder_helper(cur.right, left_arr)
            return right_arr

    # Time Complexity: O(n)
    # Space Complexity:   O(n)  
    def postorder(self): # left, right, root
        arr = []
        if self.root == None:
            return arr
        else:
            return self.postorder_helper(self.root, arr)

    def postorder_helper(self, cur, arr):
        if cur == None:
            return arr
        else:
            left_arr = self.postorder_helper(cur.left, arr)
            right_arr = self.postorder_helper(cur.right, left_arr)
            right_arr.append({ 
                        "key" : cur.key, 
                        "value" : cur.value
                        })
            return right_arr


    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def height(self):
        if self.root == None:
            return 0 
        else:
            return self.height_helper(self.root)
    
    def height_helper(self, cur):
        max_height = 0
        if cur == None: # 5 3 None
            return max_height 
        
        else:
            left_height = self.height_helper(cur.left) 
            right_height = self.height_helper(cur.right) 
            max_height = max(left_height, right_height)
            return max_height + 1


#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
# bfs - This method returns an array with the tree elements in a level-by-level order 
    def bfs(self):
        if self.root == None:
            return []
        else:
            ans = []
            node_queue = [self.root]  
            while len(node_queue) != 0: # at least one node in the queue
                cur_node = node_queue[0]  
                if cur_node.left:       
                    node_queue.append(cur_node.left)    
                if cur_node.right:
                    node_queue.append(cur_node.right)   
                ans.append(self.convert_node_to_dict(cur_node))
                node_queue.pop(0)
            return ans
            
        
            
            
    def convert_node_to_dict(self, cur):
        return {"key": cur.key,
                "value": cur.value
                }
        
        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"


tree = Tree()
tree.add(5, "Peter")
tree.add(7, "Ada")
tree.add(10, "Mary")
tree.add(3, "Dick")
tree.add(4, "Jack")


# print(tree.root.key == 5)
# print(tree.root.right.key == 7)
# print(tree.root.right.right.key == 10)
# print(tree.root.left.key == 3)
# print(tree.root.left.right.key == 4)
# print(tree.inorder())
print(tree.height())