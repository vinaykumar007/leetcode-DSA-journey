class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index={}
        for i,n in enumerate(nums):
            index[n]=i
        for i,n in enumerate(nums):
            diff=target-n
            if diff in index and index[diff]!=i:
                return [i,index[diff]]
