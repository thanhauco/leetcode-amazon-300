"""
Problem: Shortest Word Distance
Difficulty: Easy
Category: Array
LeetCode ID: 223

Description:
This is a standard problem description for Shortest Word Distance.
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
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
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
        i1, i2 = -1, -1
        min_dist = float('inf')
        for i, w in enumerate(wordsDict):
            if w == word1:
                i1 = i
            elif w == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                min_dist = min(min_dist, abs(i1 - i2))
        return min_dist

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    print(f"Test Case 1: {sol.shortestDistance(wordsDict, word1, word2)}")
