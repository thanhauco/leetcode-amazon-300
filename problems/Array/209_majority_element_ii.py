"""
Problem: Majority Element II
Difficulty: Medium
Category: Array
LeetCode ID: 209

Description:
This is a standard problem description for Majority Element II.
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
    def majorityElement(self, nums: List[int]) -> List[int]:
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
        if not nums: return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [3,2,3]
    print(f"Test Case 1: {sol.majorityElement(nums)}")
