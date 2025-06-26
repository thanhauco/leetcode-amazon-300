"""
Problem: Missing Ranges
Difficulty: Easy
Category: Array
LeetCode ID: 160

Description:
This is a standard problem description for Missing Ranges.
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
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
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
        res = []
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                if nums[i] - nums[i-1] == 2:
                    res.append(str(nums[i-1] + 1))
                else:
                    res.append(str(nums[i-1] + 1) + "->" + str(nums[i] - 1))
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(f"Test Case 1: {sol.findMissingRanges(nums, lower, upper)}")
