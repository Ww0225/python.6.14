# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。
# 请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 返回这三个数的和。
# 假定每组输入只存在恰好一个解。
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ret = float('inf')
        n = len(nums)
        for k in range(n-2):
            i,j=k+1,n-1
            while i<j:
                sum=nums[k]+nums[i]+nums[j]
                ret = sum if abs(sum-target)<abs(ret-target) else ret
                if sum==target:
                    return sum
                if sum<target:
                    i+=1
                else:
                    j-=1
        return ret