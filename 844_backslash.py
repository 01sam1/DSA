'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.parsing_logic(s)==self.parsing_logic(t)
        # return 
    def parsing_logic(self,s):
        s=list(s)
        length =len(s)
        i=0
        j=0
        flag =1
        counter =0
        while(i<length):
            word =s[i]
            if word=='#':
                j-=1
                if j<0:
                    j=0
                    counter-=1
                # else:
                #     j =i-1
                    # flag=0
                counter+=2
            # elif word=='#':
            #     j-=1
            #     counter+=2
            #     if j<0:
            #         counter-=1
            #         flag=1
            # if word!='#' and flag==0:
            #     s[j]=s[i]
            #     j+=1
            else:
                s[j]=s[i]
                j+=1
            
            i+=1
        print(s,counter)
        return ''.join(s[:length-counter])