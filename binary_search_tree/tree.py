class TreeNode:
    def __init__(self, key, val=None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n) balanced / O(n) unbalanced
    # Space Complexity: O(log n) balanced / O(n) unbalanced
    def add(self, key, value=None):
        new_node = TreeNode(key, value)

        def add_helper(curr, new):
            if curr is None:
                return new
            if new_node.key <= curr.key:
                curr.left = add_helper(curr.left, new)
            else:
                curr.right = add_helper(curr.right, new)
            return curr

        self.root = add_helper(self.root, new_node)

    # Time Complexity: O(log n) balanced / O(n) unbalanced
    # Space Complexity: O(log n) balanced / O(n) unbalanced

    def find(self, key):
        def find_helper(curr, key):
            if curr is None:
                return None
            if curr.key == key:
                return curr.value
            if key <= curr.key:
                return find_helper(curr.left, key)
            else:
                return find_helper(curr.right, key)

        return find_helper(self.root, key)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        def inorder_helper(curr, arr):
            if curr is None:
                return arr
            inorder_helper(curr.left, arr)
            arr.append({"key": curr.key, "value": curr.value})
            inorder_helper(curr.right, arr)
            return arr

        return inorder_helper(self.root, [])

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        def preorder_helper(curr, arr):
            if curr is None:
                return arr
            arr.append({"key": curr.key, "value": curr.value})
            preorder_helper(curr.left, arr)
            preorder_helper(curr.right, arr)
            return arr

        return preorder_helper(self.root, [])

    # Time Complexity: O(n)
    # Space Complexity: O(n

    def postorder(self):
        def postorder_helper(curr, arr):
            if curr is None:
                return arr
            postorder_helper(curr.left, arr)
            postorder_helper(curr.right, arr)
            arr.append({"key": curr.key, "value": curr.value})
            return arr

        return postorder_helper(self.root, [])

    # Time Complexity: O(log n) balanced / O(n) unbalanced
    # Space Complexity: O(log n) balanced / O(n) unbalanced
    def height(self):
        def height_helper(curr):
            if curr is None:
                return 0
            left_len = 1 + height_helper(curr.left)
            right_len = 1 + height_helper(curr.right)
            max_len = max(left_len, right_len)
            return max_len

        return height_helper(self.root)


#   # Optional Method
#   # Time Complexity: O(n^2)
#   # Space Complexity: O(n)

    def bfs(self):
        def bfs_helper(queue, arr):
            if queue == [] or queue[0] is None:
                return arr
            curr = queue.pop(0)
            arr.append({"key": curr.key, "value": curr.value})
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            return bfs_helper(queue, arr)

        return bfs_helper([self.root], [])


#   # Useful for printing

    def to_s(self):
        return f"{self.inorder()}"
