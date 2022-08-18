import {describe, it} from "mocha";
import TreeT from "../../../src/Tree/Tree";
import ConstructFromLevelOrder from "../../../src/Tree/ConstructFromLevelOrder/ConstructFromLevelOrder";
import InvertBinaryTree from "../../../src/Tree/InvertBinaryTree/InvertBinaryTree";
import LevelOrderTraversal from "../../../src/Tree/LevelOrderTraversal/LevelOrderTraversal";
import {expect} from "chai";

describe('Invert binary tree', () => {
  describe('exec', () => {
    it('should return correct result', () => {
      const values: number[] = [4,2,7,1,3,6,9]
      const res: number[] = [4,7,2,9,6,3,1]

      const tree: TreeT<number> = new TreeT<number>()

      const constructFromLevelOrder: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree)
      constructFromLevelOrder.exec(values)

      const invertBinaryTree: InvertBinaryTree<number> = new InvertBinaryTree<number>(tree)
      invertBinaryTree.exec(tree.root)

      const levelOrderTraversal = new LevelOrderTraversal<number>(tree)
      levelOrderTraversal.exec()

      expect(levelOrderTraversal.flatResult()).deep.equal(res)
    })
  })
})
