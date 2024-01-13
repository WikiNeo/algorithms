import {describe, it} from "mocha";
import {expect} from 'chai'
import BinarySearch from "../../src/BinarySearch/BinarySearch";

describe('Binary Search', () => {
  describe('exec', () => {

    it('should return -1 with [1, 2, 3, 4, 5] and 0', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4, 5], 0);

      expect(binarySearch.exec(),).equal(-1)
    })

    it('should return 0 with [1, 2, 3, 4, 5] and 1', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4, 5], 1);

      expect(binarySearch.exec(),).equal(0)
    })

    it('should return 1 with [1, 2, 3, 4, 5] and 2', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4, 5], 2);

      expect(binarySearch.exec(),).equal(1)
    })

    it('should return 2 with [1, 2, 3, 4, 5] and 3', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4, 5], 3);

      expect(binarySearch.exec(),).equal(2)
    })

    it('should return 3 with [1, 2, 3, 4, 5] and 4', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4, 5], 4);

      expect(binarySearch.exec(),).equal(3)
    })

    it('should return 4 with [1, 2, 3, 4, 5] and 5', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4, 5], 5);

      expect(binarySearch.exec(),).equal(4)
    })

    it('should return -1 with [1, 2, 3, 4] and 0', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4], 0);

      expect(binarySearch.exec(),).equal(-1)
    })

    it('should return 0 with [1, 2, 3, 4] and 1', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4], 1);

      expect(binarySearch.exec(),).equal(0)
    })

    it('should return 1 with [1, 2, 3, 4] and 2', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4], 2);

      expect(binarySearch.exec(),).equal(1)
    })

    it('should return 2 with [1, 2, 3, 4] and 3', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4], 3);

      expect(binarySearch.exec(),).equal(2)
    })

    it('should return 3 with [1, 2, 3, 4] and 4', () => {
      const binarySearch: BinarySearch = new BinarySearch([1, 2, 3, 4], 4);

      expect(binarySearch.exec(),).equal(3)
    })
  })
})
