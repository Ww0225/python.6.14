# 给你一个按照非递减顺序排列的整数数组nums，和一个目标值target。
# 请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值target，返回[-1, -1]。
# 你必须设计并实现时间复杂度为O(logn) 的算法解决此问题。
def lower_bound(nums:list[int],target:int)->int:
    left,right=0,len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return left
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = lower_bound(nums,target)
        if start == len(nums) or nums[start]!=target:
            return [-1,-1]
        end = lower_bound(nums,target+1)-1
        return [start,end]
