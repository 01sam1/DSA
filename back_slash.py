str1="hello"
str1= list(str1)
str2=['h','e','-b','l','l','o']

# if str1==str2 then return true
# backslash should not come at the start of character
length =len(str2)
i=0
j=-1
flag =1
counter =0
while(i<length):
    word =str2[i]
    if word=='-b' and flag ==1:
        j =i-1
        flag=0
        counter+=2
    elif word=='-b' and flag==0:
        j-=1
        counter+=2
    if word!='-b' and flag==0:
        str2[j]=str2[i]
        j+=1
    i+=1
print(str2[:length-counter])
    
    
    