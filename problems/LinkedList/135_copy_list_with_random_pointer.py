"""
Problem: Copy List with Random Pointer
Difficulty: Medium
Category: Linked List
LeetCode ID: 135

Description:
This is a standard problem description for Copy List with Random Pointer.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Linked List techniques.

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
    def reverseList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Linked List to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Linked List Logic] -> [Result]
        """
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    # Mock ListNode
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            
    head = ListNode(1, ListNode(2, ListNode(3)))
    res = sol.reverseList(head)
    print(f"Test Case 1: {res.val if res else 'None'}")
