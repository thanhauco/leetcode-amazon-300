"""
Problem: Game of Life
Difficulty: Medium
Category: Array
LeetCode ID: 247

Description:
This is a standard problem description for Game of Life.
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
    def gameOfLife(self, board: List[List[int]]) -> None:
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
        # Do not return anything, modify board in-place instead.
        ROWS, COLS = len(board), len(board[0])
        def countNeighbors(r, c):
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS):
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei
        for r in range(ROWS):
            for c in range(COLS):
                nei = countNeighbors(r, c)
                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 3
                elif nei == 3:
                    board[r][c] = 2
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    sol.gameOfLife(board)
    print(f"Test Case 1: {board}")
