class PermutationInString {
  s1: string
  s2: string

  constructor(s1: string, s2: string) {
    this.s1 = s1
    this.s2 = s2
  }

  exec(): boolean {
    // if s1 length is longer than s2, then it is not possible
    const LEN1: number = this.s1.length, LEN2: number = this.s2.length;
    if(LEN1 > LEN2) return false;

    const charToCount1: Map<string, number> = new Map<string, number>()
    const charToCount2: Map<string, number> = new Map<string, number>()

    // update s1 charToCount1
    for(let i = 0; i < LEN1; i++){
      const count: number = charToCount1.get(this.s1[i]) || 0
      charToCount1.set(this.s1[i], count + 1)
    }

    // check if we have a possible substring
    const isSameMap = (): boolean => {
      for(let [key, value] of charToCount1.entries()){
        const count2: number = charToCount2.get(key) || 0
        if(value !== count2) return false;
      }
      return true;
    }


    let left: number = 0;
    for(let right = 0; right < LEN2; right++){
      const rCount: number = charToCount2.get(this.s2[right]) || 0
      charToCount2.set(this.s2[right], rCount + 1)
      const substringLen: number = right - left + 1
      if(substringLen < LEN1){ // current substring length is less than s1.length
        continue
      } else if(substringLen === LEN1){
        if(isSameMap()) return true
      } else {   // current substring length is longer than s1.length, update left pointer char count, and +1
        const lCount: number = charToCount2.get(this.s2[left]) || 0
        charToCount2.set(this.s2[left], lCount - 1)
        left++
        if(isSameMap()) return true
      }
    }

    return false;
  }
}

export default PermutationInString
