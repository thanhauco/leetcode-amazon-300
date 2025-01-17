"""
Problem: Insert Interval
Difficulty: Medium
Category: Intervals
LeetCode ID: 18

Description:
This is a standard problem description for Insert Interval.
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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(f"Test Case 1: {sol.insert(intervals, newInterval)}")
