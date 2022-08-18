import TreeNodeT, {TreeNodeS} from "./TreeNode";

class TreeT<T> {
  root: TreeNodeT<T> | null

  constructor(root?: TreeNodeT<T>) {
    this.root = (root === undefined ? null : root)
  }
}

class TreeS {
  root: TreeNodeS | null

  constructor(root?: TreeNodeS) {
    this.root = (root === undefined ? null : root)
  }
}


export default TreeT;

export {TreeS};
