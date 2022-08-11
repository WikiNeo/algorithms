class TopKFrequentElements {
  nums: number[]
  k: number

  constructor(nums: number[], k: number) {
    this.nums = nums;
    this.k = k;
  }

  exec(): number[]{
    const numToCount: Map<number, number> = new Map<number, number>();

    // store num to count
    for(const num of this.nums){
      let count: number = numToCount.get(num) || 0;
      numToCount.set(num, count + 1);
    }

    // convert hash to pair array, sort based on second element, slice first k data, and convert the format
    return [...numToCount.entries()]
      .sort((a, b) => b[1] - a[1])
      .slice(0, this.k)
      .map(d => d[0]);

  }
}

export default TopKFrequentElements;
