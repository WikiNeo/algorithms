import BaseTreeAlgorithmT from "../BaseTreeAlgorithm";
import TreeT from "../Tree";
import TreeNodeT from "../TreeNode";

class SameTree<T> extends BaseTreeAlgorithmT<T>{
  tree2: TreeT<T>

  constructor(tree1: TreeT<T>, tree2: TreeT<T>) {
    super(tree1);
    this.tree2 = tree2
  }

  exec(): boolean {
    // result
    let res: boolean = true;

    const travel = (node1: TreeNodeT<T> | null, node2: TreeNodeT<T> | null) => {
      // early return
      if(res === false) return;
      // base case
      if(node1 === null && node2 === null) return

      // one node is null or the value is not the same
      if(node1 === null || node2 === null || node1.val !== node2.val) {
        res = false;
        return
      }

      // continue to check left & right
      travel(node1.left, node2.left)
      travel(node1.right, node2.right)
    }

    // driver
    travel(this.tree.root, this.tree2.root)

    // return result
    return res
  }
}

export default SameTree;
