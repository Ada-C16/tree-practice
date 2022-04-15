package net.sophiale.trees;

import com.sun.source.tree.Tree;

import java.sql.Array;
import java.util.*;

public class BinarySearchTree<T extends Comparable> implements GeneralTree<T> {
    TreeNode<T> mRoot;

    @Override
    public void addChildNode(T value) {
        if (mRoot == null) {
            mRoot = new TreeNode<>(value);
            return;
        }

        addRecursive(mRoot, value);
    }

    private void addRecursive(TreeNode<T> cur, T value) {
        if (value.compareTo(cur.val) == -1) {
            if (cur.children.get(0) == null) {
                TreeNode<T> node = new TreeNode<>(value);
                cur.children.add(0, node);
                return;
            }
            addRecursive(cur.children.get(0), value);
        } else {
            if (cur.children.get(1) == null) {
                TreeNode<T> node = new TreeNode<>(value);
                cur.children.add(1, node);
                return;
            }
            addRecursive(cur.children.get(1), value);
        }
    }

    @Override
    public void removeChildNode(T value) {

    }

    @Override
    public boolean findNode(T value) {
        TreeNode<T> root = mRoot;
        return findRecursive(root, value);
    }

    private boolean findRecursive(TreeNode<T> cur, T value) {
        while (cur != null) {
            if (value.compareTo(cur.val) == 0) {
                return true;
            }
            if (value.compareTo(cur.val) == -1) {
                return findRecursive(cur.children.get(0), value);
            }
            return findRecursive(cur.children.get(1), value);
        }
        return false;
    }

    @Override
    public int getHeight() {
        if (mRoot != null) {
            return getHeightBFS(mRoot);
        }
        return 0;
    }

    private int getHeightBFS(TreeNode<T> root) {
        Queue<TreeNode<T>> queue = new LinkedList<TreeNode<T>>();
        queue.offer(root);
        int height = 0;
        queue.offer(null);
        while (!queue.isEmpty()) {
            TreeNode<T> node = queue.poll();
            if (node == null) {
                if (!queue.isEmpty()) {
                    queue.offer(null);
                }
                height++;
            } else {
                if (node.children.get(0) != null) {
                    queue.offer(node.children.get(0));
                }
                if (node.children.get(1) != null) {
                    queue.offer(node.children.get(1));
                }
            }
        }
        return height;
    }

    private int getHeightRecursive(TreeNode<T> node) {
        if (node == null) {
            return 0;
        }
        return 1 + Math.max(getHeightRecursive(node.children.get(0)), getHeightRecursive(node.children.get(1)));
    }

    @Override
    public int getWidth() {
        return 0;
    }

    @Override
    public List<T> preorder() {
        return preorderRecursive(mRoot, new ArrayList<T>());
    }

    private List<T> preorderRecursive(TreeNode<T> node, List<T> values) {
        if (node == null) {
            return values;
        }
        values.add(node.val);
        preorderRecursive(node.children.get(0), values);
        preorderRecursive(node.children.get(1), values);

        return values;
    }

    private List<T> preorderIterative(TreeNode<T> root) {
        List<T> values = new ArrayList<T>();
        if (root == null) {
            return values;
        }
        Stack<TreeNode<T>> stack = new Stack<TreeNode<T>>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode<T> node = stack.pop();
            values.add(node.val);

            if (node.children.get(0) != null) {
                stack.push(node.children.get(0));
            }

            if (node.children.get(1) != null) {
                stack.push(node.children.get(1));
            }
        }
        return values;
    }

    @Override
    public List<T> inorder() {
        return inorderRecursive(mRoot, new ArrayList<T>());
    }

    private  List<T> inorderRecursive(TreeNode<T> node, List<T> values) {
        if (node == null) {
            return values;
        }
        inorderRecursive(node.children.get(0), values);
        values.add(node.val);
        inorderRecursive(node.children.get(1), values);

        return values;
    }

    private List<T> inorderIterative(TreeNode<T> root) {
        List<T> values = new ArrayList<T>();
        if (root == null) {
            return values;
        }
        Stack<TreeNode<T>> stack = new Stack<TreeNode<T>>();
        TreeNode<T> node = root;
        while (!stack.isEmpty() || node != null) {
            if (node != null) {
                stack.push(node);
                node = node.children.get(0);
            } else {
                node = stack.pop();
                values.add(node.val);
                node = node.children.get(1);
            }
        }
        return values;
    }

    @Override
    public List<T> postorder() {
        return postorderRecursive(mRoot, new ArrayList<T>());
    }

    private List<T> postorderRecursive(TreeNode<T> node, List<T> values) {
        if (node == null) {
            return values;
        }
        postorderRecursive(node.children.get(0), values);
        postorderRecursive(node.children.get(1), values);
        values.add(node.val);

        return values;
    }

    private List<T> postorderIterative(TreeNode<T> root) {
        List<T> values = new ArrayList<T>();
        if (root == null) {
            return values;
        }
        Stack<TreeNode<T>> stack = new Stack<TreeNode<T>>();
        Stack<TreeNode<T>> rightStack = new Stack<TreeNode<T>>();
        TreeNode<T> node = root;
        while (!stack.isEmpty() || node != null) {
            if (node != null) {
                if (node.children.get(0) != null) {
                    rightStack.push(node.children.get(0));
                }
                stack.push(node);
                node = node.children.get(1);
            } else {
                node = stack.peek();
                if (!rightStack.isEmpty() && node.children.get(0) == rightStack.peek()) {
                    node = rightStack.pop();
                } else {
                    values.add(node.val);
                    stack.pop();
                    node = null;
                }
            }
        }
        return values;
    }

    @Override
    public List<T> bfs() {
        List<T> values = new ArrayList<T>();
        if (mRoot != null) {
            Queue<TreeNode<T>> queue = new LinkedList<TreeNode<T>>();
            queue.offer(mRoot);
            while (!queue.isEmpty()) {
                TreeNode<T> node = queue.poll();
                values.add(node.val);
                if (node.children.get(0) != null) {
                    queue.offer(node.children.get(0));
                }
                if (node.children.get(1) != null) {
                    queue.offer(node.children.get(1));
                }
            }
        }
        return values;
    }

}
