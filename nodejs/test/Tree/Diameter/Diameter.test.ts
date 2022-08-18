import {describe, it} from "mocha";
import TreeT from "../../../src/Tree/Tree";
import ConstructFromLevelOrder from "../../../src/Tree/ConstructFromLevelOrder/ConstructFromLevelOrder";
import Diameter from "../../../src/Tree/Diameter/Diameter";
import {expect} from "chai";

describe('Diameter of binary tree', () => {
  describe('exec', () => {
    it('should return correct result', () => {
      const values: number[] = [1,2,3,4,5]
      const tree: TreeT<number> = new TreeT<number>()

      const constructFromLevelOrder: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree)
      constructFromLevelOrder.exec(values)

      const diameter: Diameter<number> = new Diameter<number>(tree)

      expect(diameter.exec()).equal(3)
    })
  })
})
