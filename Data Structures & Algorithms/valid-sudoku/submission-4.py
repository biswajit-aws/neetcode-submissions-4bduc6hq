class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap=defaultdict(list)
        colmap=defaultdict(list)
        threebthree=defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in rowmap[i]:
                    rowmap[i].append(board[i][j] )
                else:
                    return False
                if board[i][j] not in colmap[j]:
                    colmap[j].append(board[i][j] )
                else:
                    return False
                if board[i][j] not in threebthree[(i//3,j//3)]:
                    threebthree[(i//3,j//3)].append(board[i][j] )
                else:
                    return False
                
        return True
