class BinarySearch {
  nums: number[]
  target: number

  constructor(nums: number[], target: number) {
    this.nums = nums;
    this.target = target
  }

  exec(): number {
    // note how we make the index inclusive here
    let leftIndex: number = 0, rightIndex: number = this.nums.length - 1;

    while(leftIndex <= rightIndex){
      const midIndex: number = Math.floor((leftIndex + rightIndex)/2)
      if(this.nums[midIndex] === this.target){
        return midIndex
      } else if(this.target < this.nums[midIndex]){ // search the left part
        rightIndex = midIndex - 1;  // note we moe the midIndex left by 1
      } else {
        leftIndex = midIndex + 1;
      }
    }

    return -1;
  }
}

export default BinarySearch;
