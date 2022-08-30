import {BaseTreeAlgorithm} from "../BaseTreeAlgorithm";
import {TreeNode} from "../TreeNode";
import {Tree} from "../Tree";

class LCABST extends BaseTreeAlgorithm{
  p: TreeNode | null
  q: TreeNode | null

  constructor(tree: Tree, p: TreeNode | null, q: TreeNode | null) {
    super(tree);
    this.p = p
    this.q = q;
  }

  exec(): TreeNode | null {
    let cur: TreeNode | null = this.tree.root;

    // eslint-disable-next-line no-constant-condition
    while(true){
      // cur node is lees than both
      // @ts-ignore
      if(cur.val < this.p.val && cur.val < this.q.val){
        // @ts-ignore
        cur = cur.right
        // @ts-ignore
      } else if (cur.val > this.p.val && cur.val > this.q.val){
        // @ts-ignore
        cur = cur.left
      } else {
        return cur
      }
    }
  }
}

export default LCABST;
