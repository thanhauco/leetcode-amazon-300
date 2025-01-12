"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
Category: Binary Search
LeetCode ID: 12

Description:
This is a standard problem description for Search in Rotated Sorted Array.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Binary Search techniques.

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
    def search(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Binary Search to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Binary Search Logic] -> [Result]
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # Left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(f"Test Case 1: {sol.search(nums, target)}")
