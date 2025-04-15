'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2'''


# import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length =len(nums)
        freq =-1
        old_word =None
        # majority =math.ceil(length/2)
        majority =(length//2)
        
        nums.sort()
        # print(nums)
        for ele in nums:
            if ele==old_word:
                freq+=1
            else:
                # if freq>=majority:
                if freq>majority:
                    break
                old_word=ele
                freq =1
        return old_word

# best amswer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        curMajority = nums[0]
        curMajorityVotes = 0
        for num in nums:
            if num == curMajority:
                curMajorityVotes += 1
            else:
                curMajorityVotes -= 1
                if curMajorityVotes == 0:
                    curMajority = num
                    curMajorityVotes = 1
        return curMajority