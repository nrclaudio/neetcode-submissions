from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] in seen:
                    return False
                elif board[row][col] != "." and board[row][col] not in seen:
                    seen.add(board[row][col])
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] in seen:
                    return False
                elif board[row][col] != "." and board[row][col] not in seen:
                    seen.add(board[row][col])
        dict_of_sets = defaultdict(list)
        for row in range(9):
            for col in range(9):
                left_quadrant = row // 3
                right_quadrant = col // 3
                if board[row][col] in set(dict_of_sets[(left_quadrant, right_quadrant)]):
                    return False
                elif board[row][col] != "." and board[row][col] not in set(dict_of_sets[(left_quadrant, right_quadrant)]):
                    dict_of_sets[(left_quadrant, right_quadrant)].append(board[row][col])
        print(dict_of_sets)
        return True





        #column check
        #box check
        