'''
Gray Code
Problem Description

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

A gray code sequence must begin with 0.



Problem Constraints
1 <= A <= 16



Input Format
First argument is an integer A.



Output Format
Return an array of integers representing the gray code sequence.



Example Input
Input 1:

A = 2
Input 1:

A = 1


Example Output
output 1:

[0, 1, 3, 2]
output 2:

[0, 1]


Example Explanation
Explanation 1:

for A = 2 the gray code sequence is:
    00 - 0
    01 - 1
    11 - 3
    10 - 2
So, return [0,1,3,2].
Explanation 1:

for A = 1 the gray code sequence is:
    00 - 0
    01 - 1
So, return [0, 1].
'''
class Solution:
    # @param A : integer
    # @return a list of integers
    def recc(self, A):
        if A == 1:
            return ['0','1']
        ans = self.recc(A-1)
        newAns = []
        for ele in ans:
            newAns.append('0'+ele)
        for i in range(len(ans)-1,-1,-1):
            newAns.append('1'+ans[i])
        return newAns
    def convert(self,ans):
        for i in range(0, len(ans)):
            tempAns = 0
            for j in range(len(ans[i])-1,-1,-1):
                if ans[i][j]=='1':
                    tempAns += 2**(len(ans[i])-1-j)    
            ans[i] = tempAns
        return ans
    def grayCode(self, A):
        ans = self.recc(A)
        ans = self.convert(ans)
        return ans
