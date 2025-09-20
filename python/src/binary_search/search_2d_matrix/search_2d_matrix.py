"""
LeetCode 74: Search a 2D Matrix

Problem: Write an efficient algorithm that searches for a value target in an m x n integer matrix.
This matrix has the following properties:
- Integers in each row are sorted from left to right
- The first integer of each row is greater than the last integer of the previous row

Time Complexity: O(log(m * n)) where m is rows and n is columns
Space Complexity: O(1)

Key Insight: The matrix can be treated as a flattened sorted 1D array due to its properties.
We can use binary search by converting between 1D and 2D indices.
"""

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    Search for target in a 2D matrix using binary search.
    
    Args:
        matrix: 2D list of integers with sorted rows and columns
        target: Integer value to search for
        
    Returns:
        True if target exists in matrix, False otherwise
        
    Examples:
        >>> searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
        True
        >>> searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
        False
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


def searchMatrix_alternative(matrix: List[List[int]], target: int) -> bool:
    """
    Alternative approach: First find the correct row, then search within that row.
    
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
            # Target could be in this row
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


# Test cases
def test_search_matrix():
    """Test cases for the search matrix function"""
    
    # Test case 1: Target exists
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert searchMatrix(matrix1, 3) == True
    assert searchMatrix(matrix1, 11) == True
    assert searchMatrix(matrix1, 60) == True
    
    # Test case 2: Target doesn't exist
    assert searchMatrix(matrix1, 13) == False
    assert searchMatrix(matrix1, 0) == False
    assert searchMatrix(matrix1, 100) == False
    
    # Test case 3: Single element matrix
    assert searchMatrix([[1]], 1) == True
    assert searchMatrix([[1]], 2) == False
    
    # Test case 4: Single row
    assert searchMatrix([[1, 3, 5, 7]], 5) == True
    assert searchMatrix([[1, 3, 5, 7]], 6) == False
    
    # Test case 5: Single column
    assert searchMatrix([[1], [3], [5]], 3) == True
    assert searchMatrix([[1], [3], [5]], 4) == False
    
    # Test case 6: Empty matrix
    assert searchMatrix([], 1) == False
    assert searchMatrix([[]], 1) == False
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_search_matrix()
