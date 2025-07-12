"""
Problem: Rotate Array
Difficulty: Medium
Category: Array
LeetCode ID: 175

Description:
This is a standard problem description for Rotate Array.
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
    def rotate(self, nums: List[int], k: int) -> None:
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
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol.rotate(nums, k)
    print(f"Test Case 1: {nums}")
