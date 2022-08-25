class CarFleet {
  target: number
  position: number[]
  speed: number[]

  constructor(target: number, position: number[], speed: number[]) {
    this.target = target
    this.position = position
    this.speed = speed
  }

  exec(): number {
    // sort position in decreasing order paried with speed
    const data: number[][] = this.position
      .map((value, index) => [value, this.speed[index]])
      .sort((a: number[], b: number[]) => b[0] - a[0])

    // maintain a monotonic increasing stack with time
    const stack: number[] = []
    for(let [position, speed] of data){
      stack.push((this.target - position)/speed)
      const sLEN: number = stack.length
      // if we ever find a car takes more or equal time than current car, do the pop()
      if(sLEN >= 2 && stack[sLEN - 2] >= stack[sLEN - 1]){
        stack.pop()
      }
    }

    return stack.length
  }
}

export default CarFleet;
