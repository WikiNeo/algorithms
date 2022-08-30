import BaseTreeAlgorithmT from "../BaseTreeAlgorithm";
import TreeNodeT from "../TreeNode";

/**
 * A binary tree's maximum depth is the number of nodes along the longest path
 * from the root node down to the farthest leaf node.
 */
class MaxDepth<T> extends BaseTreeAlgorithmT<T>{

  exec(): number {

    const depth = (node: TreeNodeT<T> | null): number => {
      // base case
      if(node === null) return 0;

      // current depth is left depth or right depth + 1
      return Math.max(depth(node.left), depth(node.right)) + 1
    }

    return depth(this.tree.root)
  }
}

export default MaxDepth;
