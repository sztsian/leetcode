#!/usr/bin/env python3

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resultdict={}
        for i in range(len(nums)):
            if target-nums[i] in resultdict:
                return [resultdict[target-nums[i]], i]
            else:
                resultdict[nums[i]] = i
        return []

if __name__ == "__main__":
    nums = [7, 2, 7, 11, 15]
    target = 9
    solution1 = Solution().twoSum
    print(solution1(nums,target))
