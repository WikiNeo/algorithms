import {describe, it} from "mocha";
import TreeT from "../../../src/Tree/Tree";
import ConstructFromLevelOrder from "../../../src/Tree/ConstructFromLevelOrder/ConstructFromLevelOrder";
import SameTree from "../../../src/Tree/SameTree/SameTree";
import {expect} from "chai";

describe('Same tree', () => {
  describe('exec', () => {
    it('should return find the same tree', () => {
      const values1: (number | null)[] = [1, 2, 3]
      const tree1: TreeT<number> = new TreeT<number>()
      const constructFromLevelOrder1: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree1)
      constructFromLevelOrder1.exec(values1)

      const values2: (number | null)[] = [1, 2, 3]
      const tree2: TreeT<number> = new TreeT<number>()
      const constructFromLevelOrder2: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree2)
      constructFromLevelOrder2.exec(values2)

      const sameTree: SameTree<number> = new SameTree<number>(tree1, tree2)
      expect(sameTree.exec()).equal(true)
    })

    it('should identify the tree shapes are not the same', () => {

      const values1: (number | null)[] = [1, 2]
      const tree1: TreeT<number> = new TreeT<number>()
      const constructFromLevelOrder1: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree1)
      constructFromLevelOrder1.exec(values1)

      const values2: (number | null)[] = [1, null, 2]
      const tree2: TreeT<number> = new TreeT<number>()
      const constructFromLevelOrder2: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree2)
      constructFromLevelOrder2.exec(values2)

      const sameTree: SameTree<number> = new SameTree<number>(tree1, tree2)
      expect(sameTree.exec()).equal(false)
    })

    it('should identify the node values are not the same', () => {
      const values1: (number | null)[] = [1, 2, 1]
      const tree1: TreeT<number> = new TreeT<number>()
      const constructFromLevelOrder1: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree1)
      constructFromLevelOrder1.exec(values1)

      const values2: (number | null)[] = [1, 1, 2]
      const tree2: TreeT<number> = new TreeT<number>()
      const constructFromLevelOrder2: ConstructFromLevelOrder<number> = new ConstructFromLevelOrder<number>(tree2)
      constructFromLevelOrder2.exec(values2)

      const sameTree: SameTree<number> = new SameTree<number>(tree1, tree2)
      expect(sameTree.exec()).equal(false)
    })
  })
})
