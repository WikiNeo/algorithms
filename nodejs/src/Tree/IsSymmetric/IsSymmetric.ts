import {BaseTreeAlgorithmS} from "../BaseTreeAlgorithm";
import {TreeNodeS} from "../TreeNode";

/**
 * We use a queue to store level info and check both ends
 */
class IsSymmetric extends BaseTreeAlgorithmS {
  exec(): boolean {
    let queue: (TreeNodeS | null)[] = [];
    // @ts-ignore
    queue.push(this.tree.root.left);
    // @ts-ignore
    queue.push(this.tree.root.right);

    while(queue.length !== 0) {
      const LEN: number = queue.length;

      for(let i = 0; i < LEN/2; i++){
        // @ts-ignore
        let front: TreeNodeS = queue.shift();
        // @ts-ignore
        let end: TreeNodeS = queue.pop();

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
