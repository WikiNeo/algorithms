import BaseTreeAlgorithm from "../BaseTreeAlgorithm";
import TreeNodeT from "../TreeNode";

class IsBalanced<T> extends BaseTreeAlgorithm<T>{
  exec(): boolean {
    let res: boolean = true;

    const height = (node: TreeNodeT<T> | null): number => {
      if(res === false || node === null) return 0

      const left: number = height(node.left)
      const right: number = height(node.right)

      if(Math.abs(left - right) > 2) res = false;

      return Math.max(left, right) + 1
    }

    height(this.tree.root)

    return res;
  }
}

export default IsBalanced;
