import TreeNodeT from "./TreeNode";

class Tree<T> {
  root: TreeNodeT<T> | null

  constructor(root?: TreeNodeT<T>) {
    this.root = (root === undefined ? null : root)
  }
}

export default Tree;
