import {describe, it} from "mocha";
import TreeT from "../../../src/Tree/Tree";
import ConstructFromLevelOrder from "../../../src/Tree/ConstructFromLevelOrder/ConstructFromLevelOrder";
import IsBalanced from "../../../src/Tree/IsBalanced/IsBalanced";
import {expect} from "chai";

describe('isBalanced binary tree', () => {
  describe('exec', () => {
    it('should return correct result', () => {
      const values: (number | null)[] = [3, 9, 20, null, null, 15, 7]
      const tree: TreeT<number> = new TreeT<number>()

      const constructFromLevelOrder: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree)
      constructFromLevelOrder.exec(values)

      const isBalanced: IsBalanced<number> = new IsBalanced<number>(tree)

      expect(isBalanced.exec()).equal(true)
    })
  })
})
