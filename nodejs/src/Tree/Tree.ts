import TreeNodeT, {TreeNode} from "./TreeNode";

class TreeT<T> {
  root: TreeNodeT<T> | null

  constructor(root?: TreeNodeT<T>) {
    this.root = (root === undefined ? null : root)
  }
}

class Tree {
  root: TreeNode | null

  constructor(root?: TreeNode) {
    this.root = (root === undefined ? null : root)
  }
}


export default TreeT;

export {Tree};
