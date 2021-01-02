'''
Count Subarrays
Problem Description

Misha likes finding all Subarrays of an Array. Now she gives you an array A of N elements and told you to find the number of subarrays of A, that have unique elements.

Since the number of subarrays could be large, return value % 109 +7.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 106



Input Format
The only argument given is an Array A, having N integers.



Output Format
Return the number of subarrays of A, that have unique elements.



Example Input
Input 1:

 A = [1, 1, 3]
Input 2:

 A = [2, 1, 2]


Example Output
Output 1:

 4
Output 1:

 5


Example Explanation
Explanation 1:

 Subarrays of A that have unique elements only:
 [1], [1], [1, 3], [3]
Explanation 2:

 Subarrays of A that have unique elements only:
 [2], [1], [2, 1], [1, 2], [2]

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        i = 0
        j = 0
        map = {}
        answer = 0
        while i < len(A) and j < len(A):
            if A[j] in map and map[A[j]] >= i:
                i = map[A[j]]+1         
                del map[A[j]]
            map[A[j]] = j
            answer += (j-i+1)
            j += 1
        return answer%((10**9)+7)
