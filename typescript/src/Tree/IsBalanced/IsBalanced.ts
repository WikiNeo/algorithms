import BaseTreeAlgorithmT from "../BaseTreeAlgorithm";
import TreeNodeT from "../TreeNode";

class IsBalanced<T> extends BaseTreeAlgorithmT<T>{
  exec(): boolean {
    let res: boolean = true;

    const depth = (node: TreeNodeT<T> | null): number => {
      // early return & base case
      if(res === false || node === null) return 0

      // we get the depth of left & right node
      const left: number = depth(node.left)
      const right: number = depth(node.right)

      // check there difference to update result
      if(Math.abs(left - right) > 1) res = false;

      // update depth result
      return Math.max(left, right) + 1
    }

    depth(this.tree.root)

    return res;
  }
}

export default IsBalanced;
