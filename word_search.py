from typing import List
Time Complexity:  O(N * M * 4^L)  N is the number of rows, M is the number of columns, and L is the length of the word
Space Complexity: O(L)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, board, word):
                        return True
        return False

    def dfs(self, row: int, col: int, curr: int, board: List[List[str]], word: str) -> bool:
        if curr == len(word):
            return True
        rows, cols = len(board), len(board[0])
        if (row < 0 or col < 0 or row >= rows or col >= cols or 
            board[row][col] == '#' or word[curr] != board[row][col]):
            return False
        temp = board[row][col]
        board[row][col] = '#'
        result = (self.dfs(row + 1, col, curr + 1, board, word) or
                  self.dfs(row - 1, col, curr + 1, board, word) or
                  self.dfs(row, col + 1, curr + 1, board, word) or
                  self.dfs(row, col - 1, curr + 1, board, word))
        board[row][col] = temp
        return result
