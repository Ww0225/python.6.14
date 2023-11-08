# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
class Solution:
    def trap(self, height: list[int]) -> int:
        ans = left = pre_max = suf_max = 0
        left,right = 0,len(height)-1
        while left<=right:
            pre_max = max(pre_max,height[left])
            suf_max = max(suf_max,height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left+=1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans