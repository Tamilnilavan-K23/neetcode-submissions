# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=list1
        cur2=list2
        res=[]

        while cur1 :
            res.append(cur1.val)
            cur1=cur1.next

        while cur2:
            res.append(cur2.val)
            cur2=cur2.next

        if not res : return None 
        res.sort()
        head=ListNode(res[0])
        temp=head

        for i in range(1,len(res)):
               newNode=ListNode(res[i])
               temp.next=newNode
               temp=temp.next

        return head
        