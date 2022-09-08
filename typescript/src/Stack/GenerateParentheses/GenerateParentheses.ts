class GenerateParentheses {
  n: number

  constructor(n: number) {
    this.n = n
  }

  exec(): string[]{
    const res: string[] = []

    const generate = (cur: string, left: number = 0, right: number = 0): void => {
      // in the result string, we should have n left & n right brackets
      if(left === this.n && right === this.n){
        res.push(cur)
        return;
      }

      // we can add left bracket if it is less than final value
      if(left < this.n) generate(cur + '(', left + 1, right)
      // we can add right bracket if it is less than right value
      if(right < left) generate(cur + ')', left, right + 1)
    }

    generate('')

    return res;
  }
}

export default GenerateParentheses;
