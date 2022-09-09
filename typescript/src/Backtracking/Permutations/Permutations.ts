class Permutations {
  nums: number[]

  constructor(nums: number[]) {
    this.nums = nums
  }

  exec(): number[][] {
    return this.permute(this.nums)
  }

  exec2(): number[][]{
    return this.permute2(this.nums)
  }

  permute2(nums: number[]): number[][]{
    // special case handle
    if(nums.length === 1) return [[...nums]]

    const res: number[][] = []
    const LEN: number = nums.length;

    for(let i = 0; i < LEN; i++){
      const numsCopy: number[] = [...nums]
      // remove ith element
      numsCopy.splice(i, 1)
      // get permutations of the new array, and add the removed element back
      this.permute2(numsCopy).map(permutation => res.push([...permutation, nums[i]]))
    }

    return res;
  }

  permute(nums: number[]): number[][] {
    let res: number[][] = [];

    if(nums.length === 1) {
      return [[...nums]]
    }

    // for an array of length n, loop n times.
    // eslint-disable-next-line no-unused-vars
    for(let _ of nums){
      // remove the first value
      // @ts-ignore
      const first: number = nums.shift()
      // get permutation of remaining array
      const perms: number[][] = this.permute(nums)
      // add first value back
      for(let perm of perms){
        perm.push(first)
      }
      // update result
      res.push(...perms)
      // move first value to the back
      nums.push(first)
    }
    return res;
  }
}

export default Permutations
