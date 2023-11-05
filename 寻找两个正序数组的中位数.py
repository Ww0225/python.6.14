# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        len1,len2 = len(nums1),len(nums2)
        left,right,half_len = 0,len1,(len1+len2+1)//2
        mid1 = (left+right)//2
        mid2 = half_len - mid1
        while left < right:
            if mid1 < len1 and nums2[mid2-1] > nums1[mid1]:
                left = mid1 + 1
            else:
                right = mid1
            mid1 = (left+right)//2
            mid2 = half_len - mid1
        if mid1 == 0:
            max_of_left = nums2[mid2-1]
        elif mid2 == 0:
            max_of_left = nums1[mid1-1]
        else:
            max_of_left = max(nums1[mid1-1],nums2[mid2-1])
        if (len1+len2)%2==1:
            return max_of_left
        if mid1 == len1:
            min_of_right = nums2[mid2]
        elif mid2 == len2:
            min_of_right = nums1[mid1]
        else:
            min_of_right = min(nums1[mid1],nums2[mid2])
        return (max_of_left+min_of_right)/2