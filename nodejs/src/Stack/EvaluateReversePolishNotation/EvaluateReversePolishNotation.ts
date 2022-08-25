class EvaluateReversePolishNotation {
  tokens: string[]

  constructor(tokens: string[]) {
    this.tokens = tokens
  }

  exec(): number {
    const stack: number[] = [];

    for(const c of this.tokens){
      if(c === '+'){
        // @ts-ignore
        stack.push(stack.pop() + stack.pop())
      } else if(c === '-'){
        // @ts-ignore
        const first: number = stack.pop()
        // @ts-ignore
        const second: number = stack.pop();
        stack.push(second - first)
      } else if(c === '*'){
        // @ts-ignore
        stack.push(stack.pop() * stack.pop())
      } else if(c === '/'){
        // @ts-ignore
        const first: number = stack.pop()
        // @ts-ignore
        const second: number = stack.pop();
        const temp: number = second/first
        temp > 0 ? stack.push(Math.floor(temp)) : stack.push(Math.ceil(temp))
      } else {
        stack.push(parseInt(c))
      }
    }

    return stack[0]
  }
}

export default EvaluateReversePolishNotation;
