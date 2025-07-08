"""
Problem: Binary Search Tree Iterator
Difficulty: Medium
Category: Tree
LeetCode ID: 170

Description:
This is a standard problem description for Binary Search Tree Iterator.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Tree techniques.

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
    def isValidBST(self, root: Optional['TreeNode']) -> bool:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Tree to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Tree Logic] -> [Result]
        """
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    # Mock TreeNode
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Test Case 1: {sol.isValidBST(root)}")
