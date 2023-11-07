class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        place = [[set() for _ in range(3)] for _ in range(3)]
        black = []
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    black.append((i, j))
                else:
                    row[i].add(ch)
                    col[j].add(ch)
                    place[i // 3][j // 3].add(ch)

        def dfs(n):
            if n == len(black):
                return True
            i, j = black[n]
            rst = nums - row[i] - col[j] - place[i // 3][j // 3]
            if not rst:
                return False
            for num in rst:
                board[i][j] = num
                row[i].add(num)
                col[j].add(num)
                place[i // 3][j // 3].add(num)
                if dfs(n + 1):
                    return True
                row[i].remove(num)
                col[j].remove(num)
                place[i // 3][j // 3].remove(num)

        dfs(0)
