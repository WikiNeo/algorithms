class DailyTemperatures {
  temperatures: number[]

  constructor(temperatures: number[]) {
    this.temperatures = temperatures
  }

  exec(): number[]{
    const LEN: number = this.temperatures.length;
    const res: number[] = new Array(LEN).fill(0);
    // we use a monotonic increasing stack to store index of temperature
    const stack: number[] = [];

    for(let i = 0; i < LEN; i++){
      if(stack.length === 0){
        stack.push(i)
      } else {
        // while current value is larger than the top value in stack, we pop the top value to keep the monotonic property
        // of the stack and update the result
        while(this.temperatures[i] > this.temperatures[stack[stack.length - 1]]){
          const topIndex: number = stack[stack.length - 1]
          res[topIndex] = i - topIndex;
          stack.pop()
        }
        stack.push(i)
      }
    }

    return res;
  }
}

export default DailyTemperatures;
