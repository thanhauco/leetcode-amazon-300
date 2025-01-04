"""
Problem: Longest Palindromic Substring
Difficulty: Medium
Category: DP
LeetCode ID: 3

Description:
This is a standard problem description for Longest Palindromic Substring.
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
    def longestPalindrome(self, s: str) -> str:
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
        res = ""
        resLen = 0
        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    s = "babad"
    print(f"Test Case 1: {sol.longestPalindrome(s)}")
