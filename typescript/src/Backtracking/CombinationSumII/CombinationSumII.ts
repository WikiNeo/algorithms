class CombinationSumII {
  candidates: number[]
  target: number


  constructor(candidates: number[], target: number) {
    this.candidates = candidates
    this.target = target
  }

  exec(): number[][]{
    const res: number[][] = []
    const LEN: number = this.candidates.length;

    // preprocessing for skipping duplicates later
    this.candidates.sort((a: number, b: number) => a - b)

    // one solution container
    const combination: number[] = []
    const exec = (i: number, sum: number) => {
      // success condition
      if(sum === this.target) {
        res.push([...combination])
        return;
      }
      // fail condition
      if(i === LEN || sum > this.target) return;

      // include current element and move to next one
      combination.push(this.candidates[i])
      exec(i + 1, sum + this.candidates[i])

      // ignore current element and all its duplicates, and move to next one
      combination.pop()
      while(i + 1 < LEN && this.candidates[i] === this.candidates[i + 1]) i++
      exec(i + 1, sum)
    }

    exec(0, 0)

    return res;
  }
}

export default CombinationSumII;
