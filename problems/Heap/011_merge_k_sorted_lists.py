"""
Problem: Merge k Sorted Lists
Difficulty: Hard
Category: Heap
LeetCode ID: 11

Description:
This is a standard problem description for Merge k Sorted Lists.
In a real interview, you would be given specific constraints and examples.
The goal is to implement an efficient solution using Heap techniques.

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
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Analysis:
        The approach uses Heap to solve the problem efficiently.
        We iterate through the data and apply the core logic.
        
        Diagram:
        Input -> Process -> Output
        [Data] -> [Heap Logic] -> [Result]
        """
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
    
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

# Mock Data for Testing
if __name__ == "__main__":
    sol = Solution()
    
    # Mock ListNode
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    res = sol.mergeKLists(lists)
    print(f"Test Case 1: {res.val}")
