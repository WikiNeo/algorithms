import {describe, it} from "mocha";
import {expect} from "chai";
import TreeNodeT from "../../../src/Tree/TreeNode";
import TreeT from "../../../src/Tree/Tree";
import LevelOrderTraversal from "../../../src/Tree/LevelOrderTraversal/LevelOrderTraversal";

describe('level order traversal', () => {
  describe('exec', () => {
    it('should return correct result', () => {
      const root: TreeNodeT<number> = new TreeNodeT<number>(3)
      const node9: TreeNodeT<number> = new TreeNodeT<number>(9)
      const node20: TreeNodeT<number> = new TreeNodeT<number>(20)
      const node15: TreeNodeT<number> = new TreeNodeT<number>(15)
      const node7: TreeNodeT<number> = new TreeNodeT<number>(7)

      root.left = node9
      root.right = node20
      node20.left = node15
      node20.right = node7
      const tree: TreeT<number> = new TreeT<number>(root)

      const levelOrderTraversal = new LevelOrderTraversal<number>(tree)
      levelOrderTraversal.exec()

      expect(levelOrderTraversal.result).deep.equal([[3], [9, 20], [15, 7]])
    })
  })
})
