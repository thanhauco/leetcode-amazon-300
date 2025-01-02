"""
Problem: Two Sum
Difficulty: Easy
Category: Array
LeetCode ID: 1

Description:
This is a standard problem description for Two Sum.
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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
        prev_map = {}  # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        return []

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Test Case 1: {sol.twoSum(nums, target)}")
