import BaseTreeAlgorithmT from "../BaseTreeAlgorithm";
import TreeNodeT from "../TreeNode";

class ConstructFromLevelOrder<T> extends BaseTreeAlgorithmT<T>{
  exec(values: (T | null)[]){
    const queue: (TreeNodeT<T> | null)[] = []

    const insertValue = (value: T | null) => {
      const node: (TreeNodeT<T> | null) = (value === null ? null : new TreeNodeT<T>(value))

      if(this.tree.root === null) {
        this.tree.root = node
      } else {
        if(queue[0] === null){
          queue.shift()
        } else {
          if(queue[0].left === null && queue[0]?.leftAddedNull === false){
            queue[0].left = node
            queue[0]?.setLeftAddedNull()
          } else{
            queue[0].right = node
            queue.shift()
          }
        }
      }

      queue.push(node)
    }

    values.forEach(value => insertValue(value))

  }
}

export default ConstructFromLevelOrder;
