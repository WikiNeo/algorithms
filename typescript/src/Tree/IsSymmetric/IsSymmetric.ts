import {BaseTreeAlgorithm} from "../BaseTreeAlgorithm";
import {TreeNode} from "../TreeNode";

/**
 * We use a queue to store level info and check both ends
 */
class IsSymmetric extends BaseTreeAlgorithm {
  exec(): boolean {
    let queue: (TreeNode | null)[] = [];
    // @ts-ignore
    queue.push(this.tree.root.left);
    // @ts-ignore
    queue.push(this.tree.root.right);

    while(queue.length !== 0) {
      const LEN: number = queue.length;

      for(let i = 0; i < LEN/2; i++){
        // @ts-ignore
        let front: TreeNode = queue.shift();
        // @ts-ignore
        let end: TreeNode = queue.pop();

        if(front === null && end === null) continue;
        if( (front === null || end === null) || (front.val !== end.val)) return false;

        queue.unshift(front.left);
        queue.unshift(front.right);
        queue.push(end.right)
        queue.push(end.left);
      }
    }

    return true;
  }
}

export default IsSymmetric;
