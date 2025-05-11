# knuth-morris pratt algorithm
def KMP(text,pattern):
    ar =[0]*len(pattern)
    print(ar)
    i,j=1,0
    flag =0
    while(i<len(pattern)or (flag==1 and i==len(pattern)-1)):
        if pattern[j]!=pattern[i]:
            flag =1
            j-=1
            if j==-1:
                j=0
            j=ar[j]
        if pattern[j]==pattern[i] :
            flag =0
            j+=1
            ar[i]=j
        if not flag:
            i+=1
            
    return ar

def main():
    ans =KMP('','aabaabaaa')
    print(ans)
    

# main()


def temp(pattern):
    length =len(pattern)
    code =[0]*length
    i,j =1,0
    flag =0
    
    if isinstance(pattern,str):
        while(i!=length):
            if pattern[j]==pattern[i]:
                print('matched')
                
                code[i] =j+1
                i+=1
                j+=1
                # flag =1
            else:
                print('mis-matched')
                print(i)
                
                if j!=0:
                    j=code[j-1]
                    # flag =0
                    continue
                
                i+=1
                # flag=0
        return code
    else:
        return -1
# pat ="aabaabaaa"

def pattern_match(text,pattern):
    length =len(pattern)
    length_tx =len(text)
    code =temp(pattern)
    print(code)
    
    # start comparing
    # if pattern ==pattern.length that means text is matched
    # if text is not matched with pattern then set pattern from the start
    i,j =0,0 #i for text while j for pattern
    # flag =0
    matched_index =i
    while(i!=length_tx and j!=length):
        if text[i]==pattern[j]:
            i+=1
            j+=1
            # flag =1
        else:
            if j!=0:
                j =code[j-1]
                matched_index = i-j
                # flag =0
                continue
            i+=1
            matched_index =i
            
    if j==length:
        print('matched')
        print('matched index',matched_index)
    else:
        print('pattern not exist in text')
        
pat ="abcdabca"
# pattern_match('abxabcabcaby','abcaby')
pattern_match('sabhayaakshit','akshit')
# print(temp(pat))