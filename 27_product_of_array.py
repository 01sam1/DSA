'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left =1
        right =1
        left_li =[1]
        right_li =[1]
        length =len(nums)
        for i in range(1,length):
            left_li.append(left:=left*nums[i-1])
            right_li.append(right:=right*nums[length-i])
        # print(left_li,right_li)

        return [left_li[i]*right_li[length-1-i] for i in range(0,length)]
        