class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cur = []
        def backtrack(r,c,vis):
            nonlocal word
            if ''.join(cur)==word:
                return True
           
            if r<len(board) and r>-1 and c>-1 and c<len(board[r]):
                temp = board[r][c]
                n = len(cur)
                if word[n]==temp and (r,c) not in vis:
                    vis.add((r,c))
                    cur.append(temp)
                    if backtrack(r,c-1, vis) or backtrack(r,c+1,vis) or backtrack(r-1,c, vis) or backtrack(r+1,c, vis):
                        return True
                    cur.pop()
                    vis.remove((r,c))
                else:
                    return False
            else:
                return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==word[0]:
                    if backtrack(r,c,set()):
                        return True

        return False