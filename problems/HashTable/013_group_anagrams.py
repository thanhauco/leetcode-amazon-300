"""
Problem: Group Anagrams
Difficulty: Medium
Category: Hash Table
LeetCode ID: 13

Description:
This is a standard problem description for Group Anagrams.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Hash Table techniques.

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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Hash Table to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Hash Table Logic] -> [Result]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"Test Case 1: {sol.groupAnagrams(strs)}")
