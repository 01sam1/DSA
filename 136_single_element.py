'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

# import math

class Solution:
    def minheap(self,idx):
        T =idx
        self.n =len(self.nums)
        if idx*2<self.n and self.nums[idx]>self.nums[idx*2]:
            T =idx*2
        if idx*2+1<self.n and self.nums[idx*2+1]<self.nums[T]:
            T =idx*2+1
        # swap
        if T!=idx:
            temp =self.nums[idx]
            self.nums[idx] =self.nums[T]
            self.nums[T] =temp
            self.minheap(T)
    def buildHeap(self,nums):
         # create min heap
        self.nums =[0]+nums
        self.n =len(self.nums)
        for i in range(self.n//2,0,-1):
            self.minheap(i)
        # print(self.nums)
        # done buiding of heap tree
    def popEle(self):
        # print(self.n)
        if self.n>2:
            ele =self.nums[1]
            self.nums[1] =self.nums.pop()
            # print(self.nums)
            self.minheap(1)
            return ele
        return self.nums.pop()
        # return self.nums.pop()

    def singleNumber(self, nums: List[int]) -> int:
        # print(nums)
        self.buildHeap(nums)
        # print(self.nums)
        n =self.n
        # print(n)
        T =None #previous element
        for i in range(1,n):
            ele =self.popEle()
            # print(ele)
            if T==ele:
                T =None
            elif(T!=None):
                break
            else:
                T =ele
        return T
        