import {describe, it} from "mocha";
import TreeT from "../../../src/Tree/Tree";
import ConstructFromLevelOrder from "../../../src/Tree/ConstructFromLevelOrder/ConstructFromLevelOrder";
import MaxDepth from "../../../src/Tree/MaxDepth/MaxDepth";
import {expect} from "chai";

describe('Max depth of binary tree', () => {
  describe('exec', () => {
    it('should return correct result', () => {
      const values: (number | null)[] = [3,9,20,null,null,15,7]
      const tree: TreeT<number> = new TreeT<number>()

      const constructFromLevelOrder: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree)
      constructFromLevelOrder.exec(values)

      const maxDepth: MaxDepth<number> = new MaxDepth<number>(tree)

      expect(maxDepth.exec()).equal(3)
    })
  })
})
