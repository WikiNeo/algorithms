class Permutations {
  nums: number[]

  constructor(nums: number[]) {
    this.nums = nums
  }

  exec(): number[][] {
    return this.permute(this.nums)
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
