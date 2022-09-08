class LongestSubstringWithoutRepeatingCharacters {
  s: string;

  constructor(s: string) {
    this.s = s;
  }

  exec(): number {
    const LEN: number = this.s.length
    if(LEN <= 1) return LEN;

    let res: number = 0;
    let left: number = 0;
    let set: Set<string> = new Set<string>()

    for(let right = 0; right < LEN; right++){
      while(set.has(this.s[right])){
        set.delete(this.s[left])
        left++
      }
      set.add(this.s[right])
      res = Math.max(right - left + 1, res)
    }

    return res;
  }
}

export default LongestSubstringWithoutRepeatingCharacters;
