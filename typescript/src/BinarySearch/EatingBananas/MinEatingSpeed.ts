class MinEatingSpeed {
  piles: number[]
  h: number

  constructor(piles: number[], h: number) {
    this.piles = piles
    this.h = h
  }

  /**
   * We can assume a min eating speed 1, and max eating speed to be the max value in the piles
   *
   * Then we do a binary search that meets the eating time and find the possible min value
   */
  exec(): number {
    let left: number = 1, right: number = Math.max(...this.piles)
    let res: number = right;

    while(left <= right){
      const mid: number = Math.floor((left + right)/2)
      const time: number = this.piles.reduce((acc, pile) => acc + Math.ceil(pile/mid), 0)

      if(time <= this.h){
        res = Math.min(res, mid)
        right = mid - 1
      } else {
        left = mid + 1
      }
    }

    return res;
  }

}

export default MinEatingSpeed;
