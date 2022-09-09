class ThreeSum {
    nums: number[]

    constructor(nums: number[]) {
        this.nums = nums;
    }

    exec(): number[][]{
        this.nums = this.nums.sort((a, b) => a - b); // O(n log(n)) time;

        const result: number[][] = [];

        for (let i = 0; i < this.nums.length - 2; i++) {
            const num1 = this.nums[i];

            // if value on the current index is same as last index, we don't need to do any duplicate work
            if (i > 0 && num1 === this.nums[i - 1]) continue;

            let leftPointer = i + 1;
            let rightPointer = this.nums.length - 1;

            while (leftPointer < rightPointer) {
                const left = this.nums[leftPointer];
                const right = this.nums[rightPointer];
                const sum = num1 + left + right;

                if (sum === 0) {
                    result.push([num1, left, right]);
                    leftPointer++;

                    // if value on new leftPointer index is the same as last index where we found a solution
                    // we don't need to do any duplicate work, increment leftPointer until we have a new value
                    while (this.nums[leftPointer] === this.nums[leftPointer - 1]) {
                        leftPointer++;
                    }
                } else if (sum > 0) {
                    rightPointer--;
                } else {
                    leftPointer++;
                }
            }
        }

        return result;
    }

}

export default ThreeSum;