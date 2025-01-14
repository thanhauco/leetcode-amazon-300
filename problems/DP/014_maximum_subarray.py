"""
Problem: Maximum Subarray
Difficulty: Easy
Category: DP
LeetCode ID: 14

Description:
This is a standard problem description for Maximum Subarray.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using DP techniques.

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
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses DP to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [DP Logic] -> [Result]
        """
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(f"Test Case 1: {sol.maxSubArray(nums)}")
