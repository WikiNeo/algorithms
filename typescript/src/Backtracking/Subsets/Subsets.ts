class Subsets {
  nums: number[]

  constructor(nums: number[]) {
    this.nums = nums
  }

  exec(): number[][]{
    let res: number[][] = [];

    let cur: number[] = [];
    const dfs = (i: number) => {
      if(i >= this.nums.length){
        // make a copy of cur
        res.push([...cur])
        return
      }

      // we add cur index value
      cur.push(this.nums[i])
      dfs(i + 1)

      // we dont add cur inde value
      cur.pop()
      dfs(i + 1)
    }

    dfs(0)

    return res;
  }
}

export default Subsets;
