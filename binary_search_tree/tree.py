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
        added_node = TreeNode(key, value)
        if not self.root:
            self.root = added_node
            return self.root
        parent_node = self.root
        while True:
            # if the added_node is greater than the parent_node
            if added_node.key > parent_node.key:
                # if the parent_node does NOT have a right node
                if not parent_node.right:
                    parent_node.right = added_node
                    return added_node
                # if the parent_node DOES have a right node, make its right node the new parent_node 
                else:
                    parent_node = parent_node.right
            # if the added_node is less than the parent_node                
            elif added_node.key <= parent_node.key:
                # if the parent_node does NOT have a left node
                if not parent_node.left:
                    parent_node.left = added_node
                    return added_node
                # if the parent_node DOES have a left node, make its left node the new parent_node
                else:
                    parent_node = parent_node.left
            else:
                return "WTF"
                    

    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    def find(self, key):
        current_node = self.root
        while current_node:
            if key == current_node.key:
                return current_node.value
            elif key > current_node.key:
                current_node = current_node.right
            elif key < current_node.key:
                current_node = current_node.left
        return None

    # left, current, right
    def inorder_helper(self, current_node, node_list = None):
        if node_list == None:
            node_list = []
        if current_node:
            self.inorder_helper(current_node.left, node_list)
            node_list.append({
                "key" : current_node.key,
                "value" : current_node.value,
            })
            self.inorder_helper(current_node.right, node_list)
        return node_list

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        return self.inorder_helper(self.root)

    def preorder_helper(self, current_node, node_list = None):
        if node_list == None:
            node_list = []
        if current_node:
            node_list.append({
                "key" : current_node.key,
                "value" : current_node.value,
            })
            self.inorder_helper(current_node.left, node_list)
            self.inorder_helper(current_node.right, node_list)
        return node_list

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder(self):
        return self.preorder_helper(self.root)

    def postorder_helper(self, current_node, node_list = None):
        if node_list == None:
            node_list = []
        if current_node:
            self.inorder_helper(current_node.left, node_list)
            self.inorder_helper(current_node.right, node_list)
            node_list.append({
                "key" : current_node.key,
                "value" : current_node.value,
            })
        return node_list

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        return self.postorder_helper(self.root)

    def height_helper(self, current_node, node_list = None):
        if node_list == None:
            node_list = []
        if current_node:
            self.height_helper(current_node.left, node_list)
            if current_node.left == None and current_node.right == None:
                node_list.append(current_node.key)
            self.height_helper(current_node.right, node_list)
        return node_list
    
    def find_count(self, key):
        current_node = self.root
        count = 0
        while current_node:
            count += 1
            if key == current_node.key:
                return count
            elif key > current_node.key:
                current_node = current_node.right
            elif key < current_node.key:
                current_node = current_node.left
        return None

    # Time Complexity: O(nlog(n))
    # Space Complexity: O(m) where m is the number of end nodes  
    def height(self):
        ends_list = self.height_helper(self.root)
        max_height = 0
        for end_key in ends_list:
            height = self.find_count(end_key)
            if height > max_height:
                max_height = height
        return max_height

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
