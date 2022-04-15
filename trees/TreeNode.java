package net.sophiale.trees;

import java.util.ArrayList;
import java.util.List;

public class TreeNode<T extends Comparable> {
    T val = null;
    List<TreeNode<T>> children = new ArrayList<TreeNode<T>>();

    public TreeNode(T val) {
        this.val = val;
    }
}

