import BaseTreeAlgorithm from "../BaseTreeAlgorithm";
import TreeNodeT from "../TreeNode";

class InvertBinaryTree<T> extends BaseTreeAlgorithm<T>{

  exec(node: TreeNodeT<T> | null): TreeNodeT<T> | null{
    if(node === null){
      return null;
    }

    const temp: TreeNodeT<T> | null = node.left;
    node.left = node.right;
    node.right = temp;

    this.exec(node.left)
    this.exec(node.right)

    return node;
  }
}

export default InvertBinaryTree
