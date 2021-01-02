'''
Rotated Sorted Array Search
Problem Description

Given a sorted array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints
1 <= N <= 1000000

1 <= A[i] <= 10^9

all elements in A are disitinct.



Input Format
The first argument given is the integer array A.

The second argument given is the integer B.



Output Format
Return index of B in array A, otherwise return -1



Example Input
Input 1:

A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4
Input 2:

A = [1]
B = 1


Example Output
Output 1:

 0
Output 2:

 0


Example Explanation
Explanation 1:

 
Target 4 is found at index 0 in A.
Explanation 2:

 
Target 1 is found at index 0 in A.
'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def bst(self, A, start,end,key):
        ans = -1
        while start <= end:
            mid = int((start+end)/2)
            if A[mid] == key:
                ans = mid
                break
            elif A[mid]>key:
                end = mid-1
            else:
                start = mid+1
        return ans
    def search(self, A, B):
        ans = -1
        if len(A) == 1 and A[0] == B:
            ans = 0
        elif A[0]<A[len(A)-1]:
            ans = self.bst(A, 0, len(A)-1, B)
        else:
            start = 0
            end = len(A)-1
            pivot = -1
            while start<=end:
                mid = int((start+end)/2)
                if A[mid]>=A[0]:
                    start = mid+1
                elif A[mid]<=A[len(A)-1]:
                    if mid-1>=0:
                        if A[mid]<A[mid-1]:
                            pivot = mid
                            break
                        else:
                            end = mid-1
            if A[pivot] == B:
                ans = pivot
            elif A[0] == B:
                ans = 0
            elif A[len(A)-1] == B:
                ans = len(A)-1
            else:
                if B < pivot:
                    ans = self.bst(A, 0,pivot-1,B)
                else:
                    ans = self.bst(A, pivot+1, len(A)-1, B)
        return ans

