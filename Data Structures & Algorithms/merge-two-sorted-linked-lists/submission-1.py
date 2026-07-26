# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        minHeap = []
        res = ListNode()
        head = res
        while list1 != None or list2 != None or len(minHeap) != 0:
            if list1 != None:
                heapq.heappush(minHeap, list1.val)
                list1 = list1.next
            if list2 != None:
                heapq.heappush(minHeap, list2.val)
                list2 = list2.next
            curVal = ListNode(heapq.heappop(minHeap))
            # print(curVal.val, res.val)
            res.next = curVal
            res = res.next
        if head.next != None:
            head = head.next
        else:
            return None
        return head
