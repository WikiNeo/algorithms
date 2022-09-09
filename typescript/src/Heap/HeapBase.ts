interface IHeap {
  // eslint-disable-next-line no-unused-vars
  heapify(heapSize: number, i: number): void
}

abstract class HeapBase implements IHeap{
  array: number[]

  constructor(array: number[]) {
    this.array = array
  }

  // eslint-disable-next-line no-unused-vars
  abstract heapify(heapSize: number, i: number): void

  heapSort(arraySize: number) {
    // build heap (rearrange array)
    for(let i = Math.floor(arraySize/2 - 1); i >= 0; i--) this.heapify(arraySize, i)

    // one by one extract an element from heap
    for(let i = arraySize - 1; i >= 0; i--){
      // move current root to end
      this.swap(0, i)
      // call heapify on reduced map
      this.heapify(i, 0)
    }
  }

  swap(i: number, j: number){
    const temp: number = this.array[i]
    this.array[i] = this.array[j]
    this.array[j] = temp
  }
}

export default HeapBase;
