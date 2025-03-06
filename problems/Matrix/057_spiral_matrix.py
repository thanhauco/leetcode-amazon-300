"""
Problem: Spiral Matrix
Difficulty: Medium
Category: Matrix
LeetCode ID: 57

Description:
This is a standard problem description for Spiral Matrix.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Matrix techniques.

Example:
Input: ...
Output: ...

Constraints:
- 1 <= n <= 10^5
- Time Limit: 1s
"""

from typing import List, Optional, Dict, Set
import collections
import heapq
import math

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Matrix to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Matrix Logic] -> [Result]
        """
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(f"Test Case 1: {sol.spiralOrder(matrix)}")
