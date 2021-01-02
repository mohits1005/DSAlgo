'''
SIXLETS
Problem Description

Given a array of integers A of size N and an integer B.

Return number of non-empty subsequences of A of size B having sum <= 1000.



Problem Constraints
1 <= N <= 20

1 <= A[i] <= 1000

1 <= B <= N



Input Format
The first argument given is the integer array A.

The second argument given is the integer B.



Output Format
Return number of subsequences of A of size B having sum <= 1000.



Example Input
Input 1:

    A = [1, 2, 8]
    B = 2
Input 2:

    A = [5, 17, 1000, 11]
    B = 4


Example Output
Output 1:

3
Output 2:

0


Example Explanation
Explanation 1:

 {1, 2}, {1, 8}, {2, 8}
Explanation 1:

 No valid subsequence
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def recc(self, A, B, sum, length, answer, index):
        if index ==len(A):
            if sum <= 1000 and length == B:
                return answer+1
            else:
                return answer
        return self.recc(A,B,sum+A[index],length+1, answer, index+1) + self.recc(A,B,sum,length, answer, index+1) 
    def solve(self, A, B):
        ans = self.recc(A,B,0,0,0,0)
        return ans
        
