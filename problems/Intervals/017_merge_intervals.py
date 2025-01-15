"""
Problem: Merge Intervals
Difficulty: Medium
Category: Intervals
LeetCode ID: 17

Description:
This is a standard problem description for Merge Intervals.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Intervals techniques.

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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Intervals to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Intervals Logic] -> [Result]
        """
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(f"Test Case 1: {sol.merge(intervals)}")
