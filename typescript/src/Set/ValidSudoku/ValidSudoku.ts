class ValidSudoku {
    board: string[][]

    constructor(board: string[][]) {
        this.board = board
    }

    exec(): boolean {
        const LEN: number = 9
        const s: Set<string> = new Set<string>();

        for(let i = 0; i < LEN; i++){
            for(let j = 0; j < LEN; j++){
                const value: string = this.board[i][j];
                if(value === '.') continue;

                const rowKey: string = `row${i},value${value}`
                const colKey: string = `col${j},value${value}`
                const boxKey: string = `box${Math.floor(i/3)*3 + Math.floor(j/3)},value${value}`

                if(s.has(rowKey) || s.has(colKey) || s.has(boxKey)) return false;

                s.add(rowKey);
                s.add(colKey);
                s.add(boxKey)
            }
        }

        return true;
    }


}

export default ValidSudoku;
