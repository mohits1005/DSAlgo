'''
Vertical and Horizontal Sums
Problem Description

Given a matrix B, of size N x M, you are allowed to do at most A special operations on this grid such that there is no vertical or horizontal contiguous subarray that has a sum greater than C.

A special operation involves multiplying any element by -1 i.e. changing its sign.

Return 1 if it is possible to achieve the answer, otherwise 0.



Problem Constraints
1 <= N, M <= 10

0 <= A <= 5

-105 <= B[i][j], C <= 105



Input Format
The first argument is an integer A, representing the number of special operations allowed.
The second argument has the N x M integer matrix, B.
The third argument is an integer C, as described in the problem statement.



Output Format
Return 1 if it is possible to achieve the answer, otherwise 0.



Example Input
Input 1:

 A = 3
 B = [  
        [1, 1, 1]
        [1, 1, 1]
        [1, 1, 1]
     ]
 C = 2
Input 2:

 A = 1
 B = [
        [1, 1, 1]
        [1, 1, 1]
        [1, 1, 1]
     ]
 C = 2


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The given matrix does not satisfy the conditions, but if we apply the special operation to B[0][0], B[1][1], B[2][2],
 then the matrix would satisfy the given conditions i.e. no row or column has a sum greater than 2.
Explanation 2:

 It is not possible to apply the special operation to 1 element to satisfy the conditions.
'''
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def getRowColMaxArrSum(self,A,B,C,i,j):
        ## row max
        sum = 0
        start = -1
        end = -1
        rmax = 0
        for n in range(0, len(B[i])):
            if sum + B[i][n] > sum:
                if sum == 0:
                    start = n
                    end = n
                    sum = B[i][n]
                else:
                    end = n
                    sum += B[i][n]
            else:
                if sum == 0:
                    pass
                else:
                    if sum > rmax:
                        rmax = sum
                    sum = 0
                    start = -1
                    end = -1
            if n == len(B[i])-1 and end == n:
                if sum > rmax:
                    rmax = sum
        # col max
        sum = 0
        start = -1
        end = -1
        cmax = 0
        for m in range(0, len(B)):
            if sum + B[m][j] > sum:
                if sum == 0:
                    start = m
                    end = m
                    sum = B[m][j]
                else:
                    end = m
                    sum += B[m][j]
            else:
                if sum == 0:
                    pass
                else:
                    if sum > cmax:
                        cmax = sum
                    sum = 0
                    start = -1
                    end = -1
            if m == len(B)-1 and end == m:
                if sum > cmax:
                    cmax = sum
        return (rmax > C or cmax > C)
    def recc(self,A, B, C, i, j):
        if A == 0 or i == len(B) or j == len(B[0]):
            #check entire matrix
            flag = True
            for m in range(0, len(B)):
                for n in range(0, len(B[0])):
                    nflag = self.getRowColMaxArrSum(A,B,C,m,n)
                    if nflag:
                        flag = False
                        break
            if flag:
                return 1
            return 0
        #next i,j
        newi = i
        newj = j+1
        if newj == len(B[0]):
            newi += 1
            newj = 0
        #recurse
        flag = self.getRowColMaxArrSum(A,B,C,i,j)
        if flag and B[i][j] > 0:
            B[i][j] *= -1
            if self.recc(A-1, B, C, newi, newj):
                return 1
            B[i][j] *= -1
        if self.recc(A,B,C,newi,newj):
            return 1
        return 0
    def solve(self, A, B, C):
        ans = self.recc(A, B, C, 0, 0)
        return ans
