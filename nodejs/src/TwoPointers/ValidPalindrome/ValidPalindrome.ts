class ValidPalindrome {
    s: string

    constructor(s: string) {
        this.s = s;
    }

    exec(): boolean {
        this.s = this.s.toLowerCase().split('').filter(c => ('a' <= c && c <= 'z') || ('0' <= c && c <= '9')).join('')
        if (this.s.length <= 1) return true;

        let left: number = 0, right = this.s.length - 1;
        while(left < right){
            if(this.s[left] !== this.s[right]) return false;
            left++;
            right--;
        }

        return true;
    }
}

export default ValidPalindrome