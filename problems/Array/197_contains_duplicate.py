"""
Problem: Contains Duplicate
Difficulty: Easy
Category: Array
LeetCode ID: 197

Description:
This is a standard problem description for Contains Duplicate.
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
    def containsDuplicate(self, nums: List[int]) -> bool:
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
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1,2,3,1]
    print(f"Test Case 1: {sol.containsDuplicate(nums)}")
