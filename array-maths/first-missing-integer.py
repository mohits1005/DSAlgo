'''
First Missing Integer
Problem Description

Given an unsorted integer array A of size N. Find the first missing positive integer.

Note: Your algorithm should run in O(n) time and use constant space.



Problem Constraints
1 <= N <= 1000000

-109 <= A[i] <= 109



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the first missing positive integer.



Example Input
Input 1:

[1, 2, 0]
Input 2:

[3, 4, -1, 1]
Input 3:

[-8, -7, -6]


Example Output
Output 1:

3
Output 2:

2
Output 3:

1


Example Explanation
Explanation 1:

A = [1, 2, 0]
First positive integer missing from the array is 3.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(0, len(A)):
            if A[i]>0 and A[i]<=len(A):
                num = A[i]
                A[i] = 0
                backup = A[num-1]
                A[num-1] = num
                if backup != num:
                    while True:
                        if backup > 0 and backup <= len(A):
                            if A[backup-1] == 0:
                                A[backup-1] = backup
                                break
                            else:
                                temp = A[backup-1]
                                A[backup-1] = backup
                                backup = temp
                        else:
                            break   
            else:
                A[i] = 0
        foundFlag = False
        ans = None
        for i in range(0, len(A)):
            if A[i] == 0:
                ans = i+1
                foundFlag = True
                break
        if foundFlag:
            return ans
        return len(A)+1
