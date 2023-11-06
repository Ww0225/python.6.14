# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
# 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
# 请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        for k in range(len(nums)-2):
            if nums[k]>0:
                break
            if k>0 and nums[k]==nums[k-1]:
                continue
            i,j = k+1,len(nums)-1
            while i<j:
                sum = nums[k]+nums[i]+nums[j]
                if sum<0:
                    i+=1
                elif sum>0:
                    j-=1
                else:
                    res.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                    while i<j and nums[j]==nums[j+1]:
                        j+=1
        return res