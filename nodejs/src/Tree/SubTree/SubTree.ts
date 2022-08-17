import BaseTreeAlgorithm from "../BaseTreeAlgorithm";
import Tree from "../Tree";
import TreeNode from "../TreeNode";

class SubTree<T> extends BaseTreeAlgorithm<T>{
  tree2: Tree<T>

  constructor(tree1: Tree<T>, tree2: Tree<T>) {
    super(tree1);
    this.tree2 = tree2
  }

  exec(): boolean {
    const isIdentical = (node1: TreeNode<T>, node2: TreeNode<T>): boolean => {
      let identicalRes: boolean  = true;

      const travel = (node1: TreeNode<T> | null, node2: TreeNode<T> | null) => {
        if(identicalRes === false) return;
        if(node1 === null && node2 === null) return

        if(node1 === null || node2 === null || node1.value !== node2.value){
          identicalRes = false;
          return
        }
        travel(node1.left, node2.left)
        travel(node1.right, node2.right)
      }

      travel(node1, node2)

      return identicalRes;
    }

    let subtreeRes: boolean = false;

    const travelMain = (node1: TreeNode<T> | null) => {
      if(subtreeRes === true) return;
      if(node1 === null) return;

      // @ts-ignore
      if( node1.value === this.tree2.root.value && isIdentical(node1, this.tree2.root.value)){
        subtreeRes = true
        return
      }

      travelMain(node1.left)
      travelMain(node1.right)
    }

    travelMain(this.tree.root)

    return subtreeRes;
  }
}

export default SubTree
