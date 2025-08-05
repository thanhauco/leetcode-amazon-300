"""
Problem: Summary Ranges
Difficulty: Easy
Category: Array
LeetCode ID: 208

Description:
This is a standard problem description for Summary Ranges.
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
    def summaryRanges(self, nums: List[int]) -> List[str]:
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
        ranges = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if start != nums[i]:
                ranges.append(str(start) + "->" + str(nums[i]))
            else:
                ranges.append(str(start))
            i += 1
        return ranges

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [0,1,2,4,5,7]
    print(f"Test Case 1: {sol.summaryRanges(nums)}")
