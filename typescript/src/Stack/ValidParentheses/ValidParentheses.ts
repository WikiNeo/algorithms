class ValidParentheses {
  s: string;

  constructor(s: string) {
    this.s = s
  }

  exec(): boolean {
    // odd length string is surely invalid
    const LEN: number = this.s.length;
    if((LEN & 1) === 1) return false;

    const stack: string[] = [];
    for(const c of this.s){
      // store left parentheses
      if(c === '(' || c === '[' || c === '{'){
        stack.push(c)
      } else {
        // for right parentheses, get top parenthesis and check
        // @ts-ignore
        const top: string = stack.pop();
        if(!(
          (c === ')' && top === '(') ||
          (c === ']' && top === '[') ||
          (c === '}' && top === '{')
        )) {
          return false
        }
      }
    }

    // check if the stack is empty or not
    return stack.length === 0;
  }
}

export default ValidParentheses;
