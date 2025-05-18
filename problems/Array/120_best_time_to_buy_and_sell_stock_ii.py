"""
Problem: Best Time to Buy and Sell Stock II
Difficulty: Medium
Category: Array
LeetCode ID: 120

Description:
This is a standard problem description for Best Time to Buy and Sell Stock II.
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
    def maxProfit(self, prices: List[int]) -> int:
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
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    prices = [7,1,5,3,6,4]
    print(f"Test Case 1: {sol.maxProfit(prices)}")
