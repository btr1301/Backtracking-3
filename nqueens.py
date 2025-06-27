Time Complexity: O(N!)
Space Complexity: O(N)

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        temp_result = []
        self.nqueens_helper([], temp_result, 0, n)
        result = self.generate_result(temp_result, n)
        return result

    def nqueens_helper(self, current: List[int], temp_result: List[List[int]], row: int, n: int):
        if row == n:
            temp_result.append(current[:])
            return
        if row > n:
            return
        for i in range(n):
            current.append(i)
            if self.is_placing_fine(current):
                self.nqueens_helper(current, temp_result, row + 1, n)
            current.pop()

    def is_placing_fine(current: List[int]) -> bool:
        if len(current) < 2:
            return True
        else:
            row = len(current) - 1
            for i in range(row):
                if (current[row] == current[i]) or (abs(i - row) == abs(current[i] - current[row])):
                    return False
        return True

    def generate_result(temp_result: List[List[int]], n: int) -> List[List[str]]:
        temp_result_string = []
        for temp in temp_result:
            temp_string = []
            for i in range(n):
                temp_char = ['.' for _ in range(n)]
                temp_char[temp[i]] = 'Q'
                temp_string.append(''.join(temp_char))
            temp_result_string.append(temp_string)
        return temp_result_string
