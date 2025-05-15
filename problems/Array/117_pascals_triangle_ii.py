"""
Problem: Pascal's Triangle II
Difficulty: Easy
Category: Array
LeetCode ID: 117

Description:
This is a standard problem description for Pascal's Triangle II.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Array techniques.

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
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Array to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Array Logic] -> [Result]
        """
        res = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j + 1] += res[j]
            res = next_row
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    rowIndex = 3
    print(f"Test Case 1: {sol.getRow(rowIndex)}")
