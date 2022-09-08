class BestTimeToBuyAndSellStock {
  prices: number[]

  constructor(prices: number[]) {
    this.prices = prices
  }

  /**
   * We can have two pointers, and make sure the left pointer value is always less than right one.
   */
  exec(): number {
    const LEN: number = this.prices.length
    if(LEN <= 1) return 0;

    let res: number = 0;
    let left: number = 0, right: number = 1;
    while(right < LEN) {
      if(this.prices[left] > this.prices[right]) left = right;

      res = Math.max(res, this.prices[right] - this.prices[left])
      right++
    }

    return res;
  }
}

export default BestTimeToBuyAndSellStock;
