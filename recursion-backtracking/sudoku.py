'''
Sudoku
Problem Description

Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.' You may assume that there will be only one unique solution.



A sudoku puzzle,



and its solution numbers marked in red.



Problem Constraints
N = 9


Input Format
First argument is an array of array of characters representing the Sudoku puzzle.


Output Format
Modify the given input to the required answer.


Example Input
Input 1:

A = [[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]


Example Output
Output 1:

[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]


Example Explanation
Explanation 1:

Look at the diagrams given in the question.
'''
class Solution:
    # @param A : list of list of chars
    def checkRow(self,A,i,j,num):
        flag = True
        for k in range(0, len(A)):
            if A[k][j] == num:
                flag = False
                break
        return flag
    def checkColumn(self,A,i,j,num):
        flag = True
        for k in range(0, len(A[0])):
            if A[i][k] == num:
                flag = False
                break
        return flag
    def checkSubmatrix(self,A,i,j,num):
        flag = True
        rowStart = 0
        rowEnd = 0
        if i <= 2:
            rowEnd = 2
        elif i <= 5:
            rowStart = 3
            rowEnd = 5
        else:
            rowStart = 6
            rowEnd = 8
        colStart = 0
        colEnd = 0
        if j <= 2:
            colEnd = 2
        elif j <= 5:
            colStart = 3
            colEnd = 5
        else:
            colStart = 6
            colEnd = 8
        for m in range(rowStart,rowEnd+1):
            for n in range(colStart, colEnd+1):
                if A[m][n] == num:
                    flag = False
                    break
        return flag
    def findoptions(self,A,i,j):
        options = []
        for num in range(1,10):
            num = str(num)
            if self.checkRow(A,i,j,num) and self.checkColumn(A,i,j,num) and self.checkSubmatrix(A,i,j,num):
                options.append(num)
        return options
    def recc(self,A,i,j):
        if i >= len(A) or j >= len(A[0]):
            return True
        if A[i][j] != '.':
            newi = i
            newj = j+1
            if newj == len(A[0]):
                newj = 0
                newi += 1
            if self.recc(A,newi,newj):
                return True
        else:
            options = self.findoptions(A,i,j)
            if len(options) == 0:
                return
            else:
                for x in options:
                    A[i][j] = x
                    newi = i
                    newj = j+1
                    if newj == len(A[0]):
                        newj = 0
                        newi += 1
                    if self.recc(A,newi,newj):
                        return True
                    A[i][j] = '.'
    def solveSudoku(self, A):
        Matrix = [[0 for x in range(0,9)] for y in range(0,9)] 
        for i in range(0, 9):
            for j in range(0,9):
                Matrix[i][j] = A[i][j]
        self.recc(Matrix,0,0)
        for i in range(0, 9):
            for j in range(0,9):
                A[i][j] = Matrix[i][j]
        '''
        for i in range(0, 9):
            str = ""
            for j in range(0,9):
                str += A[i][j]
            A[i] = int(str)
        print(A)
        '''
        
        