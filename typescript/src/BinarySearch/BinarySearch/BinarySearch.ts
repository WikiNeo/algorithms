class BinarySearch {
  nums: number[]
  target: number

  constructor(nums: number[], target: number) {
    this.nums = nums;
    this.target = target
  }

  exec(): number {
    let left: number = 0, right: number = this.nums.length - 1;

    while(left <= right){
      const mid: number = Math.floor((left + right)/2)
      if(this.nums[mid] === this.target){
        return mid
      } else if(this.nums[mid] > this.target){
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }

    return -1;
  }
}

export default BinarySearch;
