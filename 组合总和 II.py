# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 注意：解集不能包含重复的组合。
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(state,target,choices,start,res):
            if target == 0:
                res.append(list(state))
                return
            for i in range(start,len(choices)):
                if target - choices[i] < 0:
                    break
                if i > start and choices[i] == choices[i-1]:
                    continue
                state.append(choices[i])
                backtrack(state,target-choices[i],choices,i+1,res)
                state.pop()
        state = []
        res = []
        start = 0
        candidates.sort()
        backtrack(state,target,candidates,start,res)
        return res