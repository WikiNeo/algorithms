import HeapBase from "./HeapBase";

class MinHeap extends HeapBase{
  heapify(heapSize: number, i: number) {
    this.minHeapify(heapSize, i)
  }

  minHeapify(n: number, i: number) {
    let smallest: number = i;
    let left: number = 2*i + 1
    let right: number = 2*i + 2

    // if left child is smaller than the root
    if(left < n && this.array[left] < this.array[smallest]) smallest = left
    // if right child is smaller than the smallest
    if(right < n && this.array[right] < this.array[smallest]) smallest = right

    // if smallest if not root
    if(smallest !== i){
      this.swap(i, smallest)
      // heapify the affected sub-tree
      this.minHeapify(n, smallest)
    }
  }


}

export default MinHeap;
