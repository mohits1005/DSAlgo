'''
Max Continuous Series of 1s
Problem Description

Given a binary array A, find the maximum sequence of continuous 1's that can be formed by replacing at-most B ones.

For this problem, return the indices of maximum continuous series of 1s in order.

If there are multiple possible solutions, return the sequence which has the minimum start index.



Problem Constraints
0 <= B <= 105

1 <= size(A) <= 105

A[i]==0 or A[i]==1



Input Format
First argument is an binary array A.

Second argument is an integer B.



Output Format
Return an array of integers denoting the indices(0-based) of 1's in the maximum continuous series.



Example Input
Input 1:

 A = [1 1 0 1 1 0 0 1 1 1 ]
 B = 1
Input 2:

 A = [1, 0, 0, 0, 1, 0, 1]
 B = 2


Example Output
Output 1:

 [0, 1, 2, 3, 4]
Output 2:

 [3, 4, 5, 6]


Example Explanation
Explanation 1:

 Flipping 0 present at index 2 gives us the longest continous series of 1's i.e subarray [0:4].
Explanation 2:

 Flipping 0 present at index 3 and index 5 gives us the longest continous series of 1's i.e subarray [3:6].

'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        i = 0
        j = 0
        K = B
        max = 0
        ansi = 0
        ansj = 0
        while j < len(A):
            if A[j] == 0:
                K -= 1
            if K < 0:
                if A[i] == 0:
                    K += 1
                i += 1
            if K >= 0:
                sw = len(A[i:j+1])
                if max < sw:
                    max = sw
                    ansi = i
                    ansj = j
            j += 1
        ans = []
        for k in range(ansi,ansj+1):
            ans.append(k)
        return ans
