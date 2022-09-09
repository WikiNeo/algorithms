import {BaseTreeAlgorithm} from "../BaseTreeAlgorithm";
import {TreeNode} from "../TreeNode";

class RightSideView extends BaseTreeAlgorithm{
  exec(): number[] {
    const res: number[] = []
    const queue: (TreeNode | null)[] = []
    queue.push(this.tree.root)

    while(queue.length > 0){
      const temp: number[] = []
      const LEN: number = queue.length

      for(let i = 0; i < LEN; i++){
        // @ts-ignore
        const front: TreeNode = queue.shift();
        if(front !== null){
          temp.push(front.val)
          queue.push(front.left)
          queue.push(front.right)
        }
      }

      if(temp.length > 0) res.push(temp[temp.length - 1])
    }

    return res;
  }
}

export default RightSideView;
