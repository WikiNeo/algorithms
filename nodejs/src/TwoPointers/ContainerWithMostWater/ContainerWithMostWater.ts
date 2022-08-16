class ContainerWithMostWater {
  height: number[]

  constructor(height: number[]) {
    this.height = height
  }

  /**
   * We have two pointers from left & right, and move the shorter one
   */
  exec(): number {
    let res: number = 0;
    let left: number = 0, right: number = this.height.length - 1;

    while(left < right){
      const area: number = (right - left)*Math.min(this.height[left], this.height[right]);
      res = Math.max(res, area)

      if(this.height[left] < this.height[right]){
        left++;
      } else {
        right--;
      }
    }

    return res;
  }
}

export default ContainerWithMostWater;
