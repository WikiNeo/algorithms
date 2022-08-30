import BaseTreeAlgorithmT from "../BaseTreeAlgorithm";
import TreeNodeT from "../TreeNode";

class Diameter<T> extends BaseTreeAlgorithmT<T>{
  exec(): number{
    // final result
    let res: number = 0;

    // The depth of a node in the tree is the length of the path from the root to the node.
    const depth = (node: TreeNodeT<T> | null): number => {
      // base case
      if(node === null) return 0;

      // find left & right depth
      const left: number = depth(node.left)
      const right: number = depth(node.right)

      // update result with left + right
      res = Math.max(left + right, res)

      // update depth with max value
      return Math.max(left, right) + 1
    }

    depth(this.tree.root)

    return res
  }
}

export default Diameter;
