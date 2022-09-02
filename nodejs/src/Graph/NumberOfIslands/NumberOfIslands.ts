class NumberOfIslands {
  grid: string[][]

  constructor(grid: string[][]) {
    this.grid = grid
  }

  exec(): number {
    const ROWS: number = this.grid.length;
    const COLS: number = this.grid[0].length;
    const visited: Set<string> = new Set<string>();

    // if we can find an unexplored island from (i, j), returning true
    const explore = (i: number, j: number): boolean => {
      if(i < 0 || i >= ROWS || j < 0 || j >= COLS || this.grid[i][j] === '0') return false;
      const key: string = `${i},${j}`
      if(visited.has(key)) return false;

      visited.add(key)
      explore(i, j - 1)
      explore(i - 1, j)
      explore(i, j + 1)
      explore(i + 1, j)

      return true;
    }

    let res: number = 0;
    for(let i = 0; i < ROWS; i++){
      for(let j = 0; j < COLS; j++){
        if(explore(i, j) === true) res++
      }
    }

    return res;
  }
}

export default NumberOfIslands
