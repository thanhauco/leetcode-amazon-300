"""
Problem: Container With Most Water
Difficulty: Medium
Category: Two Pointers
LeetCode ID: 4

Description:
This is a standard problem description for Container With Most Water.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Two Pointers techniques.

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
    def maxArea(self, height: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Two Pointers to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Two Pointers Logic] -> [Result]
        """
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    height = [1,8,6,2,5,4,8,3,7]
    print(f"Test Case 1: {sol.maxArea(height)}")
