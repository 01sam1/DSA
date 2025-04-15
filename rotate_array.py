a=[1,2,3,4,5,6]
length = len(a)

def rotate_engine(k:int,length):
    def inside(idx):
        return (idx+k)%length
    return inside

# k=2
# idx =0
# while(idx<length):
#     rotate_engine =(idx+2)%length
#     print(rotate_engine)
#     idx+=1

fun1 =rotate_engine(2,length)
# print(fun1(1))
buf =None
idx =0
flag =0
if length%2==0:
    a=[0]+a
    length+=1
    flag=1
    
while(a[idx]!=buf):
    if buf==None:
        buf =a[0]
    # else condition ---
    temp =fun1(idx)
    var_t =a[temp]
    a[temp] =buf
    buf =var_t
    idx =temp
print(a)

if flag:
    idx =a.index(0)
    a=a[:idx]+a[idx+1:]
print(a)

# accepted logic :
class Solution:
    def rotate_engine(self,k:int,length):
        def inside(idx):
            return (idx+k)%length
        return inside
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        if k==0 and length==1 :
            return 
        fun1 =self.rotate_engine(k,length)
        buf =nums[0]
        idx =0
        swap =0
        # main logic
        while(1):
            temp =fun1(idx)
            if temp==idx:
                swap+=1
                # continue
            else:
                var_t =nums[temp]
                nums[temp] =buf
                buf =var_t
                idx =temp
            
            if nums[idx]==buf:
                if swap==length:
                    break
                else:
                    swap-=1
                    idx =(idx+1)%length
                    buf = nums[idx]
            swap+=1
            
        
# rotate array answer :
# rotate array by K place :
class Solution:
    def rotate_engine(self,k:int,length):
        def inside(idx):
            return (idx+k)%length
        return inside
    def rotate(self, nums: List[int], k: int) -> None:
        length =len(nums)
        fun = self.rotate_engine(k,length)

        conf =fun(0) #this is an index value at first element should be place.
        j =conf
        idx =0
        remember_state =0
        counting=0

        while(counting!=length-1):
            # if idx==conf:
            #     break
            # temp =fun(idx)
            if idx!=conf:
                var_t =nums[j]
                nums[j] =nums[idx]
                nums[idx] =var_t
                j=(j+1)%length
                idx+=1
            if j==0 or j==remember_state:
                remember_state =idx
            if idx==conf:
                # idx =remember_state
                # if j>conf and length-j >conf-idx:
                #     idx =remember_state =0

                # else:
                    idx=remember_state
                
                # remember_state =conf-1
                # if j<k:
                #     remember_state =j
                # continue
            counting+=1




        
