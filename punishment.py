def dc(n):
    count =0
    i=10
    while((n:=n/i)>=1):
        count+=1
    return count+1 #added one for first digit
# print(dc(1020))      

n=36
ans =0
flag =1
while(n<37):
    square =n**2
    digit_count =dc(square)
    # print(digit_count)
    
    for i in range(1,digit_count+1):
        sub_sum = (square//(10**i)) +(square%(10**i))
        print(sub_sum)
        if sub_sum==n:
            print(n)
            ans+=square
            flag=0
            break
    if flag:
        z=square
        sum =0
        for i in range(1,digit_count+1):
              z=z//(10**i)
              sum +=z%(10**i)
        if sum==n:
            print(n)
            
            ans+=square
        flag =1
    n+=1
    
print(ans)
# not solved the problem 
# problem name = punishments number
# medium type

