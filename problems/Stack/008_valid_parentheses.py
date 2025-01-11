"""
Problem: Valid Parentheses
Difficulty: Easy
Category: Stack
LeetCode ID: 8

Description:
This is a standard problem description for Valid Parentheses.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Stack techniques.

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
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Stack to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Stack Logic] -> [Result]
        """
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    s = "()[]{}"
    print(f"Test Case 1: {sol.isValid(s)}")
