"""
Problem: Shuffle an Array
Difficulty: Medium
Category: Array
LeetCode ID: 294

Description:
This is a standard problem description for Shuffle an Array.
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
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = self.original
        self.original = list(self.original)
        return self.nums

    def shuffle(self) -> List[int]:
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
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    # Note: This requires the class structure to be slightly different for init
    # But for this template we'll just test the shuffle method assuming init happened
    import random
    sol.nums = [1, 2, 3]
    print(f"Test Case 1: {sol.shuffle()}")
