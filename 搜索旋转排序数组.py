# 整数数组nums按升序排列，数组中的值互不相同 。
# 在传递给函数之前，nums在预先未知的某个下标k（0 <= k < nums.length）上进行了旋转，
# 使数组变为[nums[k], nums[k + 1], ..., nums[n - 1], nums[0], nums[1], ..., nums[k - 1]]（下标从0开始计数）。
# 例如， [0, 1, 2, 4, 5, 6, 7]在下标3处经旋转后可能变为[4, 5, 6, 7, 0, 1, 2] 。
# 给你旋转后的数组nums和一个整数target ，如果nums中存在这个目标值target ，则返回它的下标，否则返回 - 1 。
# 你必须设计一个时间复杂度为O(logn) 的算法解决此问题。
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def is_blue(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return target > end and nums[i] >= target
            else:
                return target > end or nums[i] >= target

        left, right = 0, len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left < len(nums) and nums[left] == target else -1

