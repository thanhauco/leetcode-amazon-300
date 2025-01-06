"""
Problem: 3Sum
Difficulty: Medium
Category: Two Pointers
LeetCode ID: 5

Description:
This is a standard problem description for 3Sum.
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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [-1,0,1,2,-1,-4]
    print(f"Test Case 1: {sol.threeSum(nums)}")
