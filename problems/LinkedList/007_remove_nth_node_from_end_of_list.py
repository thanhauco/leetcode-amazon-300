"""
Problem: Remove Nth Node From End of List
Difficulty: Medium
Category: Linked List
LeetCode ID: 7

Description:
This is a standard problem description for Remove Nth Node From End of List.
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
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional['ListNode']:
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
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    # Mock ListNode
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = sol.removeNthFromEnd(head, 2)
    print(f"Test Case 1: {res.val}")
