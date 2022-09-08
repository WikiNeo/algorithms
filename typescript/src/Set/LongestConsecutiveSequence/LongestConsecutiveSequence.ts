class LongestConsecutiveSequence {
    nums: number[]

    constructor(nums: number[]) {
        this.nums = nums;
    }

    exec(): number {
        const s: Set<number> = new Set<number>(this.nums);
        let res: number = 0;

        for(let num of this.nums){
            if(s.has(num - 1)) continue;

            let temp: number = 0;
            while(s.has(num)){
                temp++;
                num++;
            }
            res = Math.max(res, temp);
        }

        return res;
    }
}


export default LongestConsecutiveSequence;