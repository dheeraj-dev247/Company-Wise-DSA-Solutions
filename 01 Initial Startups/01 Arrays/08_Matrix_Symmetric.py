"""
Matrix Symmetric
Medium
Acceptance: 56.7%

Given a square matrix, determine if it is symmetric along its main diagonal.
A matrix is symmetric if matrix[i][j] == matrix[j][i] for all valid i and j.

Examples:

    Example 1:
        Input: [[1,2,3],[2,4,5],[3,5,6]]
        Output: false
        Explanation: The matrix is not symmetric because matrix[1][2] = 4
                     but matrix[2][1] = 5.

    Example 2:
        Input: [[1,2,3],[2,1,4],[3,4,1]]
        Output: true
        Explanation: matrix[i][j] equals matrix[j][i] for all indices.

    Example 3:
        Input: [[1,2],[2,1]]
        Output: true
"""


# -------------------------------------------------
# Approach 1: Simple Check
# Just ensure matrix[i][j] == matrix[j][i]
#
# Time: O(n^2)
# Space: O(1)
# -------------------------------------------------
def is_symmetric(matrix):
    n = len(matrix)

    # If matrix is empty or single row, it is symmetric
    if n <= 1:
        return True

    for i in range(n):
        for j in range(i + 1, n):  # check only upper triangle
            if matrix[i][j] != matrix[j][i]:
                return False

    return True


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(is_symmetric([[1, 2, 3], [2, 4, 5], [3, 5, 6]]))  # False
    print(is_symmetric([[1, 2, 3], [2, 1, 4], [3, 4, 1]]))  # True
    print(is_symmetric([[1, 2], [2, 1]]))  # True
    print(is_symmetric([[1]]))  # True
    print(is_symmetric([]))  # True
