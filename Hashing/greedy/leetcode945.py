class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        summ=0
        prev=nums[0]
        # sort the array then the element will be arranged  
        # if [1,1,3,4] then when we changed by any array sum of final array answer will be same but if want to do 
        # minimum no of elemnt to affect then size-len(hashmap) 
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
        