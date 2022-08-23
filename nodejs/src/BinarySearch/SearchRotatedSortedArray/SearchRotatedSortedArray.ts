class SearchRotatedSortedArray {
  nums: number[]
  target: number

  constructor(nums: number[], target: number) {
    this.nums = nums;
    this.target = target
  }

  /**
   * We can make use of the fact part of the array is sorted and do check based on sorted portion of the array
   */
  exec(): number {
    let left: number = 0, right: number = this.nums.length - 1;

    while(left <= right){
      const mid: number = Math.floor((left + right)/2)
      if(this.nums[mid] === this.target) return mid

      // left sorted
      if(this.nums[left] <= this.nums[mid]){
        // in left sorted part
        if(this.nums[left] <= this.target && this.target < this.nums[mid]) {
          right = mid - 1
        } else {    // in right unsorted part
          left = mid + 1
        }
      } else {    // right sorted
        // in right sorted part
        if(this.nums[mid] < this.target && this.target <= this.nums[right]){
          left = mid + 1
        } else {
          right = mid - 1;
        }
      }
    }

    return -1;
  }
}

export default SearchRotatedSortedArray;
