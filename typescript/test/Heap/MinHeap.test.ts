import {describe, it} from "mocha";
import MinHeap from "../../src/Heap/MinHeap";
import {expect} from "chai";

describe('Min Heap', () => {
  describe('heapSort()', () => {
    it('should sort array in descending order', () => {
      const array: number[] = [4, 6, 3, 2, 9];
      const minHeap: MinHeap = new MinHeap(array)
      minHeap.heapSort(array.length)
      expect(array).deep.equal([9, 6, 4, 3, 2])
    })
  })
})
