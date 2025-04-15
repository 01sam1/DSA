.'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # make new node
        poi =l1
        poi2 =l2
        carry =0
        node =None
        node2=None
        first_ans_node =None
        while(poi!=None and poi2!=None):
            # print(temp_poi.val)
            ans = self.digit_engine(poi.val +poi2.val+carry)
            carry=ans[1]
            # make node ---
            # node.val =ans[0]
            node =ListNode(ans[0])
            if first_ans_node ==None:
                first_ans_node =node
            if node2!=None:
                node2.next =node
                node2=None
            node2 =node
            # change the pointer
            poi =poi.next
            poi2 =poi2.next
        if carry!=0 and poi==None and poi2==None:
            node =ListNode(carry)
            node2.next =node
            node
        elif poi!=None:
            self.unequal_linkLists(poi,node,carry)
        elif poi2!=None:
            self.unequal_linkLists(poi2,node,carry)
        return first_ans_node


    def digit_engine(self,data:int):
        if data<10:
            return (data,0)
        # manage the digit
        digit1 =data%10 #position 0
        digit2 =data//10 #position 1
        return (digit1,digit2)

    def unequal_linkLists(self,poi,node,carry):
        # flag =0
        prev_node =node
        if poi!=None:
            while(poi!=None):
                ans,carry =self.digit_engine(poi.val+carry)
                node =ListNode(ans)
                prev_node.next =node
                prev_node =node
                poi =poi.next
            if carry!=0:
                node =ListNode(carry)
                prev_node.next =node
            return node


# best answer
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        currentNode = ans

        carry = 0

        while l1 or l2:
            value = carry
            carry = 0

            if l1:
                value += l1.val
            if l2:
                value += l2.val
            
            carry = value // 10
            value = value % 10

            currentNode.next = ListNode(value)
            currentNode = currentNode.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            currentNode.next = ListNode(carry)
        
        return ans.next