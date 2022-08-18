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
    let res: boolean = true;

    const travel = (node1: TreeNodeT<T> | null, node2: TreeNodeT<T> | null) => {
      if(res === false) return;
      if(node1 === null && node2 === null) return

      if(node1 === null || node2 === null || node1.val !== node2.val) {
        res = false;
        return
      }

      travel(node1.left, node2.left)
      travel(node1.right, node2.right)
    }

    travel(this.tree.root, this.tree2.root)

    return res
  }
}

export default SameTree;
