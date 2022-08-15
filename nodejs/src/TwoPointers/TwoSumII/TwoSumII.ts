class TwoSumII {
    numbers: number[]
    target: number

    constructor(numbers: number[], target: number) {
        this.numbers = numbers;
        this.target = target
    }

    exec(): number[]{
        let left: number = 0, right: number = this.numbers.length - 1;

        while(left < right){
            const sum: number = this.numbers[left] + this.numbers[right];
            if(sum === this.target) return [left + 1, right + 1];
            sum < this.target ? left++ : right--;
        }

        return [-1, -1]
    }

}

export default TwoSumII