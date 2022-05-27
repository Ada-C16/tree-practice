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

    def add_helper(self, current_root, new_node):
        if current_root is None:
            return new_node

        if new_node.key < current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)

        else: 
            current_root.right = self.add_helper(current_root.right, new_node)
        return current_root

    def add(self, key, value = None):

        if self.root is None:
            self.root = TreeNode(key,value)
            return self.root

        new_node =TreeNode(key,value)
        self.add_helper(self.root, new_node)


    # Time Complexity: O(logn)
    # Space Complexity: O(1)

    def find(self, key):
        if self.root is None:
            return None
        current = self.root

        while current:
                if key < current.key:
                # go left
            
                    current = current.left # traversing left 
                elif key > current.key:
                
                    current = current.right # traversing right. key is the integer and value string

                else:
                    return current.value
        return None

    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def inorder_helper(self, current_node,inorder_list):
        
        if current_node is not None:
            
            # traversing left
            self.inorder_helper(current_node.left, inorder_list)
            # add current node to preorder_list
            inorder_list.append({"key": current_node.key, "value": current_node.value})
            #traversing right
            self.inorder_helper(current_node.right, inorder_list)



    def inorder(self):
        inorder_list = []
        if self.root is None:
            return inorder_list


        self.inorder_helper(self.root, inorder_list)

        return inorder_list
        # inorder = self.root
        # inorder(self.root.left)

        # inorder(self.root.right)


    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def preorder_helper(self,current_node, preorder_list):

        if current_node is not None:
            
            #append current node to preorder_list
            preorder_list.append({"key": current_node.key, "value": current_node.value})
            
            #traverse left 
            self.preorder_helper(current_node.left, preorder_list)


            #traverse right
            self.preorder_helper(current_node.right, preorder_list)




    def preorder(self):
        preorder_list = []
        if self.root is None:
            return preorder_list

        self.preorder_helper(self.root, preorder_list)

        return preorder_list
        

    #Time Complexity: O(n)
    #Space Complexity:  O(n)

    def postorder_helper(self, current_node, postorder_list):

       if current_node is not None:

           # traversing left 
           self.postorder_helper(current_node.left, postorder_list)

           #traversing right
           self.postorder_helper(current_node.right, postorder_list)

           postorder_list.append({"key": current_node.key, "value": current_node.value})


    def postorder(self):
        postorder_list = []
        if self.root is None:
            return postorder_list

        #call helper method 
        self.postorder_helper(self.root, postorder_list)

        return postorder_list

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height_helper(self,current_node):
        
        if current_node is not None:
           height_left= self.height_helper(current_node.left)
           height_right = self.height_helper(current_node.right)

        else:
            return 0

        return (max(height_left,height_right) +1)
            

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
