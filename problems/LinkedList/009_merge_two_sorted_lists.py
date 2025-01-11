"""
Problem: Merge Two Sorted Lists
Difficulty: Easy
Category: Linked List
LeetCode ID: 9

Description:
This is a standard problem description for Merge Two Sorted Lists.
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
    def mergeTwoLists(self, list1: Optional['ListNode'], list2: Optional['ListNode']) -> Optional['ListNode']:
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
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    # Mock ListNode
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    res = sol.mergeTwoLists(l1, l2)
    print(f"Test Case 1: {res.val}")
