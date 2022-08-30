import BaseTreeAlgorithmT from "../BaseTreeAlgorithm";
import TreeNodeT from "../TreeNode";

class InvertBinaryTree<T> extends BaseTreeAlgorithmT<T>{

  exec(node: TreeNodeT<T> | null): TreeNodeT<T> | null{
    // handle special case first
    if(node === null){
      return null;
    }

    // invert for current node
    const temp: TreeNodeT<T> | null = node.left;
    node.left = node.right;
    node.right = temp;

    // recursively invert left and right node
    this.exec(node.left)
    this.exec(node.right)

    // return the result
    return node;
  }
}

export default InvertBinaryTree
