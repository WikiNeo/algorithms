class SubsetsII {
  nums: number[]

  constructor(nums: number[]) {
    this.nums = nums
  }

  exec(): number[][]{
    const res: number[][] = []
    const LEN: number = this.nums.length
    this.nums.sort((a: number, b: number) => a - b)

    const exec = (i: number, subset: number[]) => {
      // success condition
      if(i === LEN) {
        res.push([...subset])
        return
      }

      // include current element
      subset.push(this.nums[i])
      exec(i + 1, subset)

      // skip current element and all its duplicates
      subset.pop()
      while(i + 1 < LEN && this.nums[i] === this.nums[i + 1]) i++;
      exec(i + 1, subset)
    }

    exec(0, [])

    return res;
  }
}

export default SubsetsII
