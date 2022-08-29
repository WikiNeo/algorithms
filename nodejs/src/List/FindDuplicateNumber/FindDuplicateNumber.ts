class FindDuplicateNumber {
  nums: number[]
  isDebug: boolean;

  constructor(nums: number[], isDebug: boolean = false) {
    this.nums = nums
    this.isDebug = isDebug
  }

  exec(): number {
    let slow: number = 0, fast: number = 0;
    if(this.isDebug) console.log(`slow = ${slow}, fast = ${fast}`)

    // move slow pointer before cycle start
    // eslint-disable-next-line no-constant-condition
    while(true){
      slow = this.nums[slow]
      fast = this.nums[this.nums[fast]]
      if(this.isDebug) console.log(`slow = ${slow}, fast = ${fast}`)
      if(slow === fast) break;
    }

    // move from start & slow until they meet
    let slow2: number = 0
    if(this.isDebug) console.log(`slow = ${slow}, slow2 = ${slow2}`)
    // eslint-disable-next-line no-constant-condition
    while(true){
      slow = this.nums[slow]
      slow2 = this.nums[slow2]
      if(this.isDebug) console.log(`slow = ${slow}, slow2 = ${slow2}`)
      if(slow === slow2) return slow
    }
  }
}

export default FindDuplicateNumber;
