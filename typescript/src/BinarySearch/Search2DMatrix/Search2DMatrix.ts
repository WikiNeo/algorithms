class Search2DMatrix {
  matrix: number[][]
  target: number

  constructor(matrix: number[][], target: number) {
    this.matrix = matrix
    this.target = target
  }

  exec(): boolean {
    const ROWS: number = this.matrix.length
    const COLS: number = this.matrix[0].length

    for(let i = 0; i < ROWS; i++){
      let left: number = 0, right: number = COLS - 1;

      if(this.matrix[i][left] <= this.target && this.target <= this.matrix[i][right]) {
        while(left <= right){
          const mid: number = Math.floor((left + right)/2)
          if(this.target === this.matrix[i][mid]) return true
          else if(this.target < this.matrix[i][mid]) right = mid - 1
          else left = mid + 1
        }
      }
    }

    return false;
  }
}

export default Search2DMatrix
