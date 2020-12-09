'''
Delete one
Problem Description

Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.

Find the maximum value of GCD.



Problem Constraints
2 <= N <= 105
1 <= A[i] <= 109



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the maximum value of GCD.



Example Input
Input 1:

 A = [12, 15, 18]
Input 2:

 A = [5, 15, 30]


Example Output
Output 1:

 6
Output 2:

 15


Example Explanation
Explanation 1:

 
 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum vallue of gcd is 6.
Explanation 2:

 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, A, B):
        gcd = 1
        if B == 0:
            return 0
        if A < B:
            A, B = B, A
        while B > 0:
            if A % B == 0:
                gcd = B
            A = A % B
            A,B = B,A
        return gcd
    def solve(self, A):
        leftgcd = [0 for elem in A]
        leftgcd[0] = A[0]
        for i in range(1, len(A)):
            leftgcd[i] = self.gcd(leftgcd[i-1],A[i])
        rightgcd = [0 for elem in A]
        rightgcd[len(A)-1] = A[len(A)-1]
        for i in range(len(A)-2, -1, -1):
            rightgcd[i] = self.gcd(rightgcd[i+1],A[i])
        maxgcd = 0
        ans = 0
        for i in range(0, len(A)):
            if i == 0:
                if rightgcd[1]>maxgcd:
                    maxgcd = rightgcd[1]
                    ans = 0
            elif i == len(A)-1:
                if leftgcd[len(A)-2]>maxgcd:
                    maxgcd = rightgcd[len(A)-2]
                    ans = len(A)-1
            else:
                commongcd = self.gcd(leftgcd[i-1],rightgcd[i+1])
                if commongcd > maxgcd:
                    maxgcd = commongcd
                    ans = i
        return A[ans]
