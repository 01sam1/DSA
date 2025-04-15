'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
'''

class Solution:
    def algorithm(self,st1,st2,idx,idx2,ans):
        if bool:=idx2==len(st2) or idx==len(st1):
            if bool:
                return ans
            return -1

        if st1[idx]==st2[idx2]:
            if ans==-1:
                ans =idx
            return self.algorithm(st1,st2,idx+1,idx2+1,ans)
        else:
            return -1


    def strStr(self, haystack: str, needle: str) -> int:
        ans =-1
        idx =0
        while(ans==-1 and idx<=len(haystack)-len(needle)):
            ans =self.algorithm(haystack,needle,idx,0,ans)
            idx+=1
        return ans

# best answer ------
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # if (needle not in haystack):
        #     return -1
        
        indexes=list()
        n=len(needle)

        l=0
        r=len(haystack)
        while (l<=r):
            if (haystack[l:l+n] == needle):
                return l
            else:
                l+=1
        return -1