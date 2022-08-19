class LongestRepeatingCharacterReplacement {
  s: string;
  k: number;

  constructor(s: string, k: number) {
    this.s = s;
    this.k = k
  }

  exec(): number{

    let res: number = 0;
    let charToCount: Map<string, number> = new Map<string, number>();

    let left: number = 0;
    charToCount.set(this.s[left], 1);
    for(let right = 0; right < this.s.length; ){
      const max: number = Math.max(...charToCount.values())
      const LEN: number = right - left + 1;

      // move left pointer
      if(LEN - max > this.k){
        let count: number = charToCount.get(this.s[left]) || 0
        charToCount.set(this.s[left], count - 1)
        left++
      } else {
        res = Math.max(res, LEN)
        right++
        let count: number = charToCount.get(this.s[right]) || 0
        charToCount.set(this.s[right], count + 1)
      }
    }

    return res;
  }

  exec2(): number {
    const LEN: number = this.s.length;
    let res: number = 0;
    let charToCount: Map<string, number> = new Map<string, number>();
    let maxCount: number = 0;
    let left: number = 0;

    for(let right = 0; right < LEN; right++){
      // update right pointer count
      let rCount = charToCount.get(this.s[right]) || 0
      rCount++;
      charToCount.set(this.s[right], rCount)

      // update max count and calculate toReplace
      maxCount = Math.max(maxCount, rCount)
      const toReplace: number = right - left + 1 - maxCount

      // check if we want to update result or move left pointer
      if(toReplace <= this.k) {
        res = Math.max(res, right - left + 1)
      } else {
        let lCount = charToCount.get(this.s[left]) || 0
        lCount--
        charToCount.set(this.s[left], lCount)
        left++
      }

    }

    return res;
  }

}

export default LongestRepeatingCharacterReplacement;
