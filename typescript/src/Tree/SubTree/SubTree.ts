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

    /**
     * Check if two trees are the same
     *
     * @param node1
     * @param node2
     */
    const isIdentical = (node1: TreeNodeT<T>, node2: TreeNodeT<T>): boolean => {
      // assume true
      let identicalRes: boolean  = true;

      const travel = (node1: TreeNodeT<T> | null, node2: TreeNodeT<T> | null) => {
        // early return
        if(identicalRes === false) return;
        // base case
        if(node1 === null && node2 === null) return

        // false case
        if(node1 === null || node2 === null || node1.val !== node2.val){
          identicalRes = false;
          return
        }

        // continue left & right
        travel(node1.left, node2.left)
        travel(node1.right, node2.right)
      }

      travel(node1, node2)

      return identicalRes;
    }

    // default false
    let subtreeRes: boolean = false;
    const travelMain = (node1: TreeNodeT<T> | null) => {
      // early return & base case
      if(subtreeRes === true) return;
      if(node1 === null) return;

      // current node value is the same and is identical
      // @ts-ignore
      if( node1.val === this.tree2.root.value && isIdentical(node1, this.tree2.root)){
        subtreeRes = true
        return
      }

      // continue left & right travel
      travelMain(node1.left)
      travelMain(node1.right)
    }

    travelMain(this.tree.root)

    return subtreeRes;
  }
}

export default SubTree
