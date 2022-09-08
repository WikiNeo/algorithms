class WordSearch {
  board: string[][]
  word: string

  constructor(board: string[][], word: string) {
    this.board = board
    this.word = word
  }

  exec(): boolean {
    // it is always good to know the dimension of the 2D board
    const ROW: number = this.board.length;
    const COL: number = this.board[0].length;

    // we always need a set for dfs
    const visited: Set<string> = new Set<string>();

    const dfs = (row: number, col: number, index: number): boolean => {
      // recursive call always has base case
      // good one
      if(index === this.word.length) return true
      // bad one
      const key: string = `${row},${col}`;
      if(row < 0 || row >= ROW || col < 0 || col >= COL || visited.has(key) || this.board[row][col] !== this.word[index]) return false;

      // recursive call here
      visited.add(key)
      let res: boolean = ( dfs(row, col - 1, index + 1) ||
        dfs(row - 1, col, index + 1) ||
        dfs(row, col + 1, index + 1) ||
        dfs(row + 1, col, index + 1))
      visited.delete(key)
      return res;
    }

    // driver logic
    for(let i = 0; i < ROW; i++){
      for(let j = 0; j < COL; j++){
        if(dfs(i, j, 0) === true) {
          return true
        }
      }
    }

    return false;
  }

}

export default WordSearch;
