'''
Find a peak element
Problem Description

Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.

For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return the peak element.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
Input 2:

A = [5, 17, 100, 11]


Example Output
Output 1:

 5
Output 2:

 100


Example Explanation
Explanation 1:

 5 is the peak.
Explanation 2:

 100 is the peak.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        start = 0
        end = len(A)-1
        ans = 0
        if len(A) == 1:
            return A[0]
        elif A[0]>A[1]:
            return A[0]
        elif A[len(A)-1]>A[len(A)-2]:
            return A[len(A)-1]
        else:
            while start <= end:
                mid = int((start+end)/2)
                if A[mid]>=A[mid-1] and A[mid]>=A[mid+1]:
                    ans = A[mid]
                    break
                elif A[mid]<A[mid-1]:
                    end = mid - 1
                else:
                    start = mid + 1
            return ans
