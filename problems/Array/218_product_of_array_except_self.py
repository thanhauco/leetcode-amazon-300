"""
Problem: Product of Array Except Self
Difficulty: Medium
Category: Array
LeetCode ID: 218

Description:
This is a standard problem description for Product of Array Except Self.
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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1,2,3,4]
    print(f"Test Case 1: {sol.productExceptSelf(nums)}")
