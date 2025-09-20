function searchMatrix(matrix: number[][], target: number): boolean {
  const ROWS: number = matrix.length;
  const COLS: number = matrix[0].length;

  for (let i = 0; i < ROWS; i++) {
    let l: number = 0, r = COLS - 1;
    // in current row
    if (matrix[i][l] <= target && target <= matrix[i][r]) {
      while (l <= r) {
        const mid: number = Math.floor((l + r) / 2);
        if (matrix[i][mid] === target) {
          return true
        }
        if (matrix[i][mid] < target) {
          l = mid + 1
        } else {
          r = mid - 1
        }
      }
    } else {
      continue;
    }
  }

  return false;
};
