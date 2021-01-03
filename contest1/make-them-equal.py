'''
Problem DescriptionYou are given an array A of length N. In one operation you can select an index i ( 1 <= i <= N ) and change A[i] to floor(A[i]/2). floor(x) is the largest integer not greater than x. 
We want to make all the elements of the array equal. Calculate the minimum number of operations needed to do so.

Problem Constraints1 <= N <= 105
1 <= A[i] <= 2 × 109

Input FormatThe first and only argument contains an integer array A of length N.Output FormatReturn the minimum number of operations to make all the elements of the array equal.Example Input
  Input 1:

  A : [ 3, 1, 1, 3 ]

Input 2:

  A : [ 2, 2, 2 ]

Example Output
  Output 1:

  2

Output 2:

  0

Example Explanation
  Explanation 1:

  We can do an operation on index 1 and 4 to change the array to [1, 1, 1, 1]

Explanation 2:

  All the elements are already same.
  '''
  class Solution:
    # @param A : list of integers
    # @return an integer
    
        
    def solve(self, A):
        map = {}
        max = 0
        maxn = 0
        for i in range(0, len(A)):
            num = A[i]
            while num:
                if num in map:
                    map[num] += 1
                else:
                    map[num] = 1
                if map[num] > max:
                    max = map[num]
                    maxn = num
                num /= 2
        ans = 0
        for i in range(0, len(A)):
            count = 0
            while A[i]:
                if A[i] == maxn:
                    break
                count += 1
                A[i] /= 2
            ans += count
        return ans