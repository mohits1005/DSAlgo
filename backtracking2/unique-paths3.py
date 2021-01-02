'''
Unique Paths III
Problem Description

Given a matrix of integers A of size N x M . There are 4 types of squares in it:

1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.
Find and return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints
2 <= N * M <= 20
-1 <= A[i] <= 2



Input Format
The first argument given is the integer matrix A.



Output Format
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example Input
Input 1:

A = [   [1, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 2, -1]   ]
Input 2:

A = [   [0, 1]
        [2, 0]    ]


Example Output
Output 1:

2
Output 2:

0


Example Explanation
Explanation 1:

We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Explanation 1:

Answer is evident here.
'''
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def recc(self,A, x, y, seen,spaces,ans):
        if x < 0 or y < 0 or x == len(A) or y == len(A[0]):
            return
        if A[x][y] == 2 and len(seen)-2==spaces:
            ans[0]+=1
            return
        #top
        if x-1 >= 0 and (A[x-1][y] == 0 or A[x-1][y] == 2) and [x-1,y] not in seen:
            seen.append([x-1,y])
            self.recc(A,x-1,y,seen,spaces, ans)
            seen.pop()
        #right
        if y+1 < len(A[0]) and (A[x][y+1] == 0 or A[x][y+1] == 2) and [x,y+1] not in seen:
            seen.append([x,y+1])
            self.recc(A,x,y+1,seen,spaces, ans)
            seen.pop()
        #bottom
        if x+1 < len(A) and (A[x+1][y] == 0 or A[x+1][y] == 2) and [x+1,y] not in seen:
            seen.append([x+1,y])
            self.recc(A,x+1,y,seen,spaces, ans)
            seen.pop()
        #left
        if y-1 >= 0 and (A[x][y-1] == 0 or A[x][y-1] == 2) and [x,y-1] not in seen:
            seen.append([x,y-1])
            self.recc(A,x,y-1,seen,spaces, ans)
            seen.pop()
    def solve(self, A):
        x = 0
        y = 0
        spaces = 0
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == 1:
                    x = i
                    y = j
                if A[i][j] == 0:
                    spaces += 1
        ans = [0]
        self.recc(A,x,y, [[x,y]], spaces, ans)
        return ans[0]
        
        
