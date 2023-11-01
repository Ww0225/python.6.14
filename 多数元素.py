# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        vote = 0
        x = 0
        for num in nums:
            if vote == 0:
                x = num
            vote += 1 if num == x else -1
        return x