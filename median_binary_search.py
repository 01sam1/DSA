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
    low =0
    high =l1_len
    while(low<high):
        # flag =(l1_len+l2_len)%2 #flag =0 if total length is even else retunr 1 for odd
        partition_x =int((low+high+1) / 2)
        partition_y =int((l1_len+l2_len+1) / 2 -partition_x )
    
        if partition_x==0:
            return l2[partition_y-1]
        elif partition_y==0:
            return l1[partition_x-1]
        
        if l1[partition_x-1]<=l2[partition_y] and l1[partition_x]>=l2[partition_y-1]:
            if (l1_len+l2_len)%2!=0:
                return max(l1[partition_x-1],l2[partition_y-1])
            else:
                # print(l1[partition_x],l2[partition_y])
                # print(l1[partition_x-1],l2[partition_y-1])
                return (max(l1[partition_x-1],l2[partition_y-1])+min(l1[partition_x],l2[partition_y]))/2
        
        elif l1[partition_x-1]>l2[partition_y]:
            high-=1
        else:
            low+=1
            
    
    
    
    

def main():
    # li1 =[1,3,8,9,15]
    # li2 =[7,11,18,19,21]
    li1 =[1,3,7,8,9]
    li2 =[11,15,18,19,21,25]
    ans =findMedian(li1,li2)
    print(ans)
    
main()