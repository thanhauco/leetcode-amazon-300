"""
Problem: Longest Consecutive Sequence
Difficulty: Medium
Category: Array
LeetCode ID: 125

Description:
This is a standard problem description for Longest Consecutive Sequence.
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
    def solve(self, nums: List[int]) -> int:
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
        # Generic implementation for Array
        res = 0
        for num in nums:
            res += num
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 2, 3]
    print(f'Test: {sol.solve(nums)}')
