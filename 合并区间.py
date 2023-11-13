# 以数组intervals表示若干个区间的集合，其中单个区间为intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 示例1：
# 输入：intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# 输出：[[1, 6], [8, 10], [15, 18]]
# 解释：区间[1, 3]和[2, 6]重叠, 将它们合并为[1, 6].
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for x,y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x,y])
            else:
                res[-1][1] = max(y,res[-1][1])
        return res