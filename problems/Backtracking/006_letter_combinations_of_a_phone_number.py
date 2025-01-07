"""
Problem: Letter Combinations of a Phone Number
Difficulty: Medium
Category: Backtracking
LeetCode ID: 6

Description:
This is a standard problem description for Letter Combinations of a Phone Number.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Backtracking techniques.

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
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Backtracking to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Backtracking Logic] -> [Result]
        """
        res = []
        digitToChar = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        if digits:
            backtrack(0, "")
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    digits = "23"
    print(f"Test Case 1: {sol.letterCombinations(digits)}")
