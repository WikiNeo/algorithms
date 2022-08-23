class MinRotatedSortedArray {
  nums: number[]

  constructor(nums: number[]) {
    this.nums = nums
  }

  exec(): number {
    let res: number = this.nums[0]
    let left: number = 0, right: number = this.nums.length - 1

    while(left <= right){
      // we are in a sorted interval, nums[left] is the potential min
      if(this.nums[left] <= this.nums[right]){
        res = Math.min(res, this.nums[left])
        break
      }

      const mid: number = Math.floor((left + right)/2)
      res = Math.min(res, this.nums[mid])

      // try to do the binary search
      if(this.nums[left] <= this.nums[mid]) left = mid + 1
      else right = mid - 1
    }

    return res;
  }
}

export default MinRotatedSortedArray;
