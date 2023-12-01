class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = {}
        for index, val in enumerate(order):
            table[val] = index

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if table[words[i][j]] > table[words[i + 1][j]]: return False

                    break

        return True