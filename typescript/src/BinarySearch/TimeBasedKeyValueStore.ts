class TimeBasedKeyValueStore {
  /**
   * We use map to store key to values
   */
  keyToValues: Map<string, [string, number][]>;

  constructor() {
    this.keyToValues = new Map<string, [string, number][]>()
  }

  /**
   * Set pair of [value, timestamp] with key
   *
   * @param key
   * @param value
   * @param timestamp
   */
  set(key: string, value: string, timestamp: number): void {
    const values: [string, number][] = this.keyToValues.get(key) || []
    values.push([value, timestamp])
    this.keyToValues.set(key, values);
  }

  get(key: string, timestamp: number): string {
    let res: string = '';
    const values: [string, number][] = this.keyToValues.get(key) || []
    let left: number = 0, right: number = values.length - 1;

    // we do binary search for the values
    while(left <= right){
      const mid: number = Math.floor((left + right)/2)

      // we update result when we ever find a timestamp_prev that is less than the timestamp
      if(values[mid][1] <= timestamp){
        res = values[mid][0]
        left = mid + 1
      } else {
        right = mid - 1;
      }
    }

    return res;
  }
}

export default TimeBasedKeyValueStore;
