# take 2 shorted list
# formula for partition
# handle edge cases
# return the answer
# remember : list1.length <list2.length
def findMedian(l1,l2):
    if len(l1)>len(l2):
        t =l1
        l1 =l2
        l2 =t
    # main logic
    l1_len =len(l1)
    l2_len =len(l2)
    flag =(l1_len+l2_len)%2 #flag =0 if total length is even else retunr 1 for odd
    partition_x =(l1_len+1) / 2 if l1_len%2!=0 else l1_len/2
    partition_y =(l1_len+l2_len+1) / 2 -partition_x  if l2_len%2!=0 else l2_len/2 -partition_x
    
    if partition_x==0:
        if flag:
            ans =((l1_len+l2_len)//2 + (l1_len+l2_len+1)//2)/2
            return ans
        else:
            
    
    
    
    

def main():
    li1 =[]
    li2 =[]
    findMedian(li1,li2)
    