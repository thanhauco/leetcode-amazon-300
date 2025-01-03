"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
Category: Sliding Window
LeetCode ID: 2

Description:
This is a standard problem description for Longest Substring Without Repeating Characters.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Sliding Window techniques.

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
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Sliding Window to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Sliding Window Logic] -> [Result]
        """
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    s = "abcabcbb"
    print(f"Test Case 1: {sol.lengthOfLongestSubstring(s)}")
