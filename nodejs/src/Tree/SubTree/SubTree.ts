import BaseTreeAlgorithmT from "../BaseTreeAlgorithm";
import TreeT from "../Tree";
import TreeNodeT from "../TreeNode";

class SubTree<T> extends BaseTreeAlgorithmT<T>{
  tree2: TreeT<T>

  constructor(tree1: TreeT<T>, tree2: TreeT<T>) {
    super(tree1);
    this.tree2 = tree2
  }

  exec(): boolean {
    const isIdentical = (node1: TreeNodeT<T>, node2: TreeNodeT<T>): boolean => {
      let identicalRes: boolean  = true;

      const travel = (node1: TreeNodeT<T> | null, node2: TreeNodeT<T> | null) => {
        if(identicalRes === false) return;
        if(node1 === null && node2 === null) return

        if(node1 === null || node2 === null || node1.val !== node2.val){
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

    const travelMain = (node1: TreeNodeT<T> | null) => {
      if(subtreeRes === true) return;
      if(node1 === null) return;

      // @ts-ignore
      if( node1.val === this.tree2.root.value && isIdentical(node1, this.tree2.root.value)){
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
