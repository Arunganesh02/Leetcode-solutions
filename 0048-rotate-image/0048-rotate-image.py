class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for column in range(len(matrix)):
            for row in range(column,len(matrix)):
                matrix[row][column],matrix[column][row] = matrix[column][row],matrix[row][column]
                row+=1
        for row in range(len(matrix)):
            col1 = 0
            col2 = len(matrix[row])-1
            while col1<=col2:
                matrix[row][col1],matrix[row][col2] = matrix[row][col2],matrix[row][col1]
                col1+=1
                col2-=1


    