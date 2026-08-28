class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        summ=0
        prev=nums[0]
        
        for i in range(1,len(nums)):
            if prev<nums[i]:
                summ+=0
                prev=nums[i]
            else:
                summ+=abs(prev+1-nums[i])
                nums[i]=prev+1
                prev=nums[i]
        return summ   
        """
        :type nums: List[int]
        :rtype: int
        """
        