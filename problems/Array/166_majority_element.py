"""
Problem: Majority Element
Difficulty: Easy
Category: Array
LeetCode ID: 166

Description:
This is a standard problem description for Majority Element.
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
    def majorityElement(self, nums: List[int]) -> int:
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
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [3,2,3]
    print(f"Test Case 1: {sol.majorityElement(nums)}")
