# Search a 2D Matrix - LeetCode 74

## Problem Description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right
- The first integer of each row is greater than the last integer of the previous row

**Example 1:**
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Example 2:**
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

## Thinking Process

### Problem Analysis
The key constraints are:
1. Each row is sorted in ascending order
2. The first element of each row is greater than the last element of the previous row

**Critical Insight:** These constraints mean the entire matrix forms a sorted sequence when viewed linearly. This allows us to treat the matrix as a flattened 1D sorted array.

### Approach Considerations

**Option 1: Naive Search** - O(m×n) time
- Search every element linearly
- Too slow for large matrices

**Option 2: Binary Search on Each Row** - O(m×log n) time  
- For each row, binary search for the target
- Better but not optimal

**Option 3: Treat as Flattened Sorted Array** - O(log(m×n)) time ✅
- The matrix properties allow us to conceptually flatten it into a 1D sorted array
- Use binary search on this virtual 1D array
- Convert between 1D indices and 2D coordinates as needed

### Visual Example

```
Matrix:              Virtual 1D Array:
[1,  3,  5,  7]      [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
[10, 11, 16, 20]  →  indices: 0, 1, 2, 3, 4,  5,  6,  7,  8,  9, 10, 11
[23, 30, 34, 60]     
```

### Index Mapping Strategy

For a matrix with `m` rows and `n` columns:
- **1D index to 2D coordinates:** `(index // n, index % n)`
- **2D coordinates to 1D index:** `row * n + col`

## Solution Implementation

### Main Approach: Flattened Array Binary Search

```python
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    Search for target in a 2D matrix using binary search.
    
    Time Complexity: O(log(m * n))
    Space Complexity: O(1)
    """
    # Handle edge cases
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D coordinates
        row = mid // n
        col = mid % n
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return False
```

### Alternative Approach: Two-Step Binary Search

```python
def searchMatrix_alternative(matrix: List[List[int]], target: int) -> bool:
    """
    Alternative: First find the correct row, then search within that row.
    
    Time Complexity: O(log m + log n) = O(log(m * n))
    Space Complexity: O(1)
    """
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    
    # Binary search to find the correct row
    top, bottom = 0, m - 1
    while top <= bottom:
        mid_row = (top + bottom) // 2
        
        if matrix[mid_row][0] <= target <= matrix[mid_row][n - 1]:
            break
        elif matrix[mid_row][0] > target:
            bottom = mid_row - 1
        else:
            top = mid_row + 1
    else:
        return False
    
    # Binary search within the found row
    target_row = (top + bottom) // 2
    left, right = 0, n - 1
    
    while left <= right:
        mid_col = (left + right) // 2
        mid_value = matrix[target_row][mid_col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid_col + 1
        else:
            right = mid_col - 1
    
    return False
```

## Row-by-Row Binary Search Analysis

### Common Alternative: TypeScript Row-by-Row Approach

Many developers intuitively implement a **row-by-row binary search** approach. Here's a typical implementation:

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
    const ROWS: number = matrix.length;
    const COLS: number = matrix[0].length;
    
    for(let i = 0; i < ROWS; i++){
        let l: number = 0, r = COLS - 1;
        // in current row
        if(matrix[i][l] <= target && target <= matrix[i][r]){
            while(l <= r){
                const mid: number = Math.floor((l + r)/2);
                if(matrix[i][mid] === target){
                    return true
                }
                if(matrix[i][mid] < target){
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
}
```

### Algorithm Analysis

**What it does:**
1. Iterates through each row sequentially
2. For each row, checks if target could be in that row (between first and last elements)
3. If target might be in the row, performs binary search on that row
4. Returns true if found, false otherwise

### Time Complexity Comparison

| Approach | Time Complexity | Explanation |
|----------|-----------------|-------------|
| **Row-by-Row Solution** | `O(m × log n)` | Checks each row + binary search per row |
| **Optimal Flattened Array** | `O(log(m × n))` | Single binary search on flattened array |

**Performance Example:**
For a 1000×1000 matrix:
- Row-by-row: ~1000 × 10 = 10,000 operations
- Optimal: ~20 operations

### Issues with Basic Row-by-Row Implementation

**1. Missing Edge Case Handling:**
```typescript
// ❌ This will crash if matrix is empty
const COLS: number = matrix[0].length;
```

**2. Missed Early Termination:**
```typescript
// Since first element of each row > last element of previous row,
// we can stop early if target < matrix[i][0]
```

**3. Logic Inefficiency:**
The `else { continue; }` is unnecessary since we're at the end of the loop.

### Improved Row-by-Row Version

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
    // Handle edge cases
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) {
        return false;
    }
    
    const ROWS: number = matrix.length;
    const COLS: number = matrix[0].length;
    
    for (let i = 0; i < ROWS; i++) {
        // Early termination: if target is less than first element,
        // it won't be in this or any subsequent rows
        if (target < matrix[i][0]) {
            break;
        }
        
        // Check if target could be in current row
        if (matrix[i][0] <= target && target <= matrix[i][COLS - 1]) {
            let l: number = 0, r: number = COLS - 1;
            
            while (l <= r) {
                const mid: number = Math.floor((l + r) / 2);
                
                if (matrix[i][mid] === target) {
                    return true;
                } else if (matrix[i][mid] < target) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            
            // If we searched the correct row and didn't find it, target doesn't exist
            return false;
        }
    }
    
    return false;
}
```

### When Each Approach is Better

**Row-by-Row Approach:**
- ✅ More intuitive and easier to understand
- ✅ Good if target is often found in early rows
- ✅ Easier to implement without index mapping knowledge
- ✅ Natural decomposition of the problem
- ❌ Worse worst-case performance O(m × log n)

**Optimal Flattened Array Approach:**
- ✅ Better worst-case performance O(log(m × n))
- ✅ More elegant and mathematically optimal
- ✅ Scales better with large matrices
- ✅ Preferred for competitive programming
- ❌ Requires understanding of index mapping
- ❌ Less intuitive for beginners

### Performance Comparison Examples

| Matrix Size | Row-by-Row (worst case) | Optimal | Improvement |
|-------------|------------------------|---------|-------------|
| 10×10 | 10 × 3 = 30 ops | ~7 ops | 4.3x faster |
| 100×100 | 100 × 7 = 700 ops | ~13 ops | 54x faster |
| 1000×1000 | 1000 × 10 = 10,000 ops | ~20 ops | 500x faster |

### Final Recommendation

**For LeetCode/Interviews:** 
Use the **optimal O(log(m×n)) flattened array approach** because:
- It demonstrates deeper algorithmic thinking
- Shows ability to exploit problem constraints fully
- Better performance characteristics
- Expected optimal solution

**For Learning/Practice:**
The **row-by-row approach** is valuable for:
- Building intuition about the problem
- Understanding binary search fundamentals
- Creating working solutions quickly
- Educational purposes

### Key Insights

1. **Both solutions are correct** - the difference is in optimization level
2. **Problem constraints matter** - the matrix properties enable the optimal approach
3. **Readability vs Performance** - sometimes there's a trade-off to consider
4. **Algorithmic progression** - moving from good to optimal often involves recognizing deeper patterns

The step from the row-by-row approach to the optimal solution demonstrates the evolution from **"make it work"** to **"make it optimal"** - both valuable skills in software development.

## Complexity Analysis

### Main Approach (Flattened Array)
- **Time Complexity:** O(log(m × n))
  - Single binary search over m × n elements
- **Space Complexity:** O(1)
  - Only constant extra space for variables

### Alternative Approach (Two-Step)
- **Time Complexity:** O(log m + log n) = O(log(m × n))
  - O(log m) to find correct row + O(log n) to search within row
- **Space Complexity:** O(1)
  - Only constant extra space for variables

## Test Cases

```python
def test_search_matrix():
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    
    # Target exists
    assert searchMatrix(matrix1, 3) == True
    assert searchMatrix(matrix1, 11) == True
    assert searchMatrix(matrix1, 60) == True
    
    # Target doesn't exist
    assert searchMatrix(matrix1, 13) == False
    assert searchMatrix(matrix1, 0) == False
    assert searchMatrix(matrix1, 100) == False
    
    # Edge cases
    assert searchMatrix([[1]], 1) == True
    assert searchMatrix([[1]], 2) == False
    assert searchMatrix([], 1) == False
    assert searchMatrix([[]], 1) == False
```

## Key Takeaways

1. **Leverage Problem Constraints:** The sorted properties of both rows and columns allow treating the matrix as a single sorted array.

2. **Index Conversion is Key:** The ability to convert between 1D and 2D indices efficiently enables the flattened array approach.

3. **Binary Search Optimization:** Instead of multiple searches, we can achieve optimal O(log(m×n)) time with a single binary search.

4. **Edge Case Handling:** Always check for empty matrices and invalid inputs.

5. **Alternative Approaches:** Sometimes multiple valid approaches exist - the two-step method is more intuitive but achieves the same time complexity.

This solution efficiently leverages the matrix's sorted properties to achieve logarithmic time complexity, making it optimal for large datasets.
