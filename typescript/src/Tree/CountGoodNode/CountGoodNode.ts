import {TreeNode} from "../TreeNode";
import {BaseTreeAlgorithm} from "../BaseTreeAlgorithm";

class CountGoodNode extends BaseTreeAlgorithm{
  exec(): number {
    if(this.tree.root === null) return 0;

    let res: number = 0;

    const travel = (node: TreeNode, max: number): void => {
      if(node === null) return;

      if(node.val >= max) res++;
      if(node.left !== null) travel(node.left, Math.max(max, node.left.val))
      if(node.right !==null) travel(node.right, Math.max(max, node.right.val))
    }

    travel(this.tree.root, this.tree.root.val)

    return res;
  }
}

export default CountGoodNode;
