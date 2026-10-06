class Solution(object):
    def twoSum(self, nums, target):
    
        hashset={}
        for i,n in enumerate(nums):
            difference=target-n
            if difference in hashset:
                return [hashset[difference],i]
            hashset [n]=i