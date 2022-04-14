package net.sophiale.trees;

import net.sophiale.trees.TreeNode;

import java.util.List;

public interface GeneralTree<T extends Comparable> {
    void addChildNode(T value);

    void removeChildNode(T value);

    boolean findNode(T value);

    int getHeight();

    int getWidth();

    List<T> preorder();

    List<T> inorder();

    List<T> postorder();

    List<T> bfs();
}
