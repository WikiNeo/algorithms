import {describe, it} from "mocha";
import TreeT from "../../../src/Tree/Tree";
import ConstructFromLevelOrder from "../../../src/Tree/ConstructFromLevelOrder/ConstructFromLevelOrder";
import LevelOrderTraversal from "../../../src/Tree/LevelOrderTraversal/LevelOrderTraversal";
import {expect} from "chai";

describe('construct binary tree from level order', () => {
  describe('exec', () => {
    it('should return correct result', () => {
      const tree: TreeT<number> = new TreeT<number>()

      const constructFromLevelOrder: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree)
      constructFromLevelOrder.exec([3, null, 20, null, null, 15, 7])

      const levelOrderTraversal = new LevelOrderTraversal<number>(tree)
      levelOrderTraversal.exec()
      // expect(levelOrderTraversal.result).deep.equal([[3], [20], [15, 7]])
    })

    it('should return correct result 2', () => {
      const tree: TreeT<number> = new TreeT<number>()

      const constructFromLevelOrder: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree)
      constructFromLevelOrder.exec([1, null, 2])

      const levelOrderTraversal = new LevelOrderTraversal<number>(tree)
      levelOrderTraversal.exec()
      expect(levelOrderTraversal.result).deep.equal([[1], [2]])
    })
  })
})
