class CombinationSum {
  candidates: number[]
  target: number

  constructor(candidates: number[], target: number) {
    this.candidates = candidates
    this.target = target
  }

  exec(): number[][]{
    const LEN: number = this.candidates.length;
    const res: number[][] = []

    // candidate stores one potential result
    const candidate: number[] = []
    const dfs = (i: number, remain: number): void => {
      // fail condition
      if(i === LEN || remain < 0) return;
      // success condition
      if(remain === 0){
        res.push([...candidate])
      }

      // using current number & stay
      candidate.push(this.candidates[i])
      dfs(i, remain - this.candidates[i])

      // not using current number & move to next
      candidate.pop()
      dfs(i + 1, remain - this.candidates[i])
    }

    dfs(0, this.target)

    return res;
  }

  exec2(): number[][] {
    const res: number[][] = []
    const LEN: number = this.candidates.length;

    const cur: number[] = []
    const dfs = (i: number, sum: number): void => {
      // we have finsihed the iteration
      if(i >= LEN || sum > this.target) return;
      // we have found result
      if(sum === this.target){
        res.push([...cur])
        return;
      }

      // include i and repeat
      cur.push(this.candidates[i])
      dfs(i, sum + this.candidates[i])

      // not include i and continue
      cur.pop()
      dfs(i + 1, sum)
    }

    dfs(0, 0)

    return res;
  }
}

export default CombinationSum;
