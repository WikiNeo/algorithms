import TreeNodeT from "../TreeNode";
import BaseTreeAlgorithmT from "../BaseTreeAlgorithm";

class LevelOrderTraversal<T> extends BaseTreeAlgorithmT<T>{

  exec() {
    if(this.tree.root === null) {
      return
    }
    const queue: (TreeNodeT<T> | null)[] = [this.tree.root]

    while(queue.length > 0){
      const temp: T[] = []
      // at the beginning of the while loop, queue stores nodes for the level
      const LEN: number = queue.length;

      for(let i = 0; i < LEN; i++){
        // get first LEN element in queue
        // @ts-ignore
        const front: TreeNodeT<T> = queue.shift()
        // add the value to temp & left/right node to queue if current node is not null
        if(front !== null){
          // @ts-ignore
          temp.push(front.val)
          queue.push(front.left)
          queue.push(front.right)
        }
      }

      if(temp.length > 0){
        this.result.push(temp)
      }
    }
  }
}

export default LevelOrderTraversal
