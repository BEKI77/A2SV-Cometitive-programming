class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]
        temp = [i[::-1] for i in temp]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=temp[i][j]
                