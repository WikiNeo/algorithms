class GroupAnagrams {
  strs: string[]

  constructor(strs: string[]) {
    this.strs = strs
  }

  /**
   * we will use sorted string as key
   */
  exec(): string[][] {
    const h: Map<string, string[]> = new Map<string, string[]>();

    for(let str of this.strs){
      const key: string = str.split('').sort().join('')
      const data: string[] = h.get(key) || []
      data.push(str)
      h.set(key, data)
    }

    return [...h.values()]
  }
}

export default GroupAnagrams;
