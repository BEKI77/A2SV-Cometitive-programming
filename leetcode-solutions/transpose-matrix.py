class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[i[j] for i in matrix] for j in range(len(matrix[0]))]