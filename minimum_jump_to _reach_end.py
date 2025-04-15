jump_ =[2,3,1,1,2,4,2,0,1,1]
length =len(jump_)

def algo(i,jump):
    if i>=length:
        return length
    if i==length-1 :
        return jump
    ans =[]
    for idx in range(1,jump_[i]+1):
        # ans.append((algo(i+idx,jump+1),i))
        ans.append(algo(i+idx,jump+1))
    a =min(ans) if ans else length
    return a

# print(algo(0,0))

# l =[(2,3),(2,2)]
# print(min(l))

def dynamic_approach():
    # i,j=1,0
    jp =[0]+[length]*(length-1)
    path=[0]*length
    
    for i in range(1,length):
        j=0
        while(j<i):
            if j+jump_[j]>=i and (T:=jp[j]+1)<jp[i]:
                jp[i] =T
                path[i]=j
            j+=1
    print(jp)
    def print_path():
        i =length-1
        print(path)
        while(i>0):
            print(i+1,end=' ')
            i =path[i]
        print(1)
        
    print_path()
    
    
    return jp[-1] if jp[-1]!=length else "infinite"

print(dynamic_approach())
    