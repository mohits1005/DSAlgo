'''
NQueens
Problem Description

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer A, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.



Problem Constraints
1 <= A <= 10



Input Format
First argument is an integer n denoting the size of chessboard



Output Format
Return an array consisting of all distinct solutions in which each element is a 2d char array representing a unique solution.



Example Input
Input 1:

A = 4
Input 2:

A = 1


Example Output
Output 1:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Output 1:

[
 [Q]
]


Example Explanation
Explanation 1:

There exist only two distinct solutions to the 4-queens puzzle:
Explanation 1:

There exist only one distinct solutions to the 1-queens puzzle:
'''
class Solution:
    # @param A : integer
    # @return a list of list of strings
    def checkRow(self,B,rowIndex, i):
        flag = True
        for j in range(0, len(B)):
            if B[j][i] == 'Q':
                flag = False
                break
        return flag
    def checkColumn(self,B,rowIndex, i):
        flag = True
        for j in range(0, len(B[rowIndex])):
            if B[rowIndex][j] == 'Q':
                flag = False
                break
        return flag
    def checkLeftDiagonal(self,B,rowIndex, i):
        flag = True
        m, n = rowIndex , i
        while m >= 0 and n>=0:
            if B[m][n] == 'Q':
                flag = False
                break
            m -= 1
            n -= 1
        if flag:
            m, n = rowIndex , i
            while m < len(B) and n< len(B[rowIndex]):
                if B[m][n] == 'Q':
                    flag = False
                    break
                m += 1
                n += 1
        return flag
    def checkRightDiagonal(self,B,rowIndex, i):
        flag = True
        m, n = rowIndex , i
        while m >= 0 and n< len(B[rowIndex]):
            if B[m][n] == 'Q':
                flag = False
                break
            m -= 1
            n += 1
        if flag:
            m, n = rowIndex , i
            while m < len(B) and n>=0:
                if B[m][n] == 'Q':
                    flag = False
                    break
                m += 1
                n -= 1
        return flag
    def check(self,B,rowIndex, i):
        return self.checkRow(B,rowIndex, i) and self.checkColumn(B,rowIndex, i) and self.checkLeftDiagonal(B,rowIndex, i) and self.checkRightDiagonal(B,rowIndex, i)
    def nqueen(self,A,B,rowIndex,ans):
        if rowIndex >= A:
            ans.append([[B[i][j] for j in range(0,A)] for i in range(0,A)])
            return
        for i in range(0, A):
            if self.check(B,rowIndex,i):
                B[rowIndex][i] = 'Q'
                self.nqueen(A,B,rowIndex+1,ans)
                B[rowIndex][i] = '.'
    def solveNQueens(self, A):
        B = [['.' for i in range(0,4)] for i in range(0,4)]
        ans = []
        self.nqueen(A,B,0,ans)
        for subans in ans:
            for i in range(0, A):
                str = ""
                for j in range(0, A):
                    str+=subans[i][j]
                subans[i] = str
        return ans
        
        
        
