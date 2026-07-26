# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        head = ListNode()
        res = head

        while True:
            for i, lst in enumerate(lists):
                if lst != None:
                    heapq.heappush(minHeap, lst.val)
                    lists[i] = lst.next
            if len(minHeap) == 0:
                break
            curVal = ListNode(heapq.heappop(minHeap))
            res.next = curVal
            res = res.next

        
        if head.next == None:
            return None
        return head.next