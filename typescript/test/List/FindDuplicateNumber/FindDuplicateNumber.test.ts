import {describe, it} from "mocha";
import {expect} from 'chai'
import FindDuplicateNumber from "../../../src/List/FindDuplicateNumber/FindDuplicateNumber";

describe('Find duplicate number', () => {
  describe('exec', () => {
    it('should return 2 with [1, 3, 4, 2, 2]', () => {
      const findDuplicateNumber = new FindDuplicateNumber([1, 3, 4, 2, 2])

      expect(findDuplicateNumber.exec()).equal(2)
    })

    it('should return 3 with [3, 1, 3, 4, 2]', () => {
      const findDuplicateNumber = new FindDuplicateNumber([3, 1, 3, 4, 2])

      expect(findDuplicateNumber.exec()).equal(3)
    })
  })
})
