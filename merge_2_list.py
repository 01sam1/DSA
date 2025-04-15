'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node =ListNode()
        ans =node
        temp_node=ListNode(110)
        flag =0
        p1 =list1
        p2 =list2
        while p1 and p2:
            if p1.val<=p2.val:
                node.next =temp=ListNode(p1.val)
                node =temp
                p1 =p1.next
            else:
                node.next =temp=ListNode(p2.val) 
                node =temp
                p2 =p2.next
        # for remaining nodes
        if not p1:
                self.remainingNode(p2,node)
        if not p2:
                self.remainingNode(p1,node)
            
        return ans.next

    def remainingNode(self,poi,node):
            while poi:
                node.next =temp=ListNode(poi.val) 
                node =temp
                poi =poi.next
                
# best solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res = head_temp = ListNode(-101)

        while list1 and list2:
            if list1.val <= list2.val:
                head_temp.next = list1
                head_temp = head_temp.next
                list1 = list1.next
            else:
                head_temp.next = list2
                head_temp = head_temp.next
                list2 = list2.next
            
        if list1:
            head_temp.next = list1
        if list2:
            head_temp.next = list2
        return res.next