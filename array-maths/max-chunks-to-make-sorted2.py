'''
Max Chunks To Make Sorted II
Problem Description

Given an array of integers (not necessarily distinct) A, if we split the array into some number of "chunks" (partitions), and individually sort each chunk. After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?



Problem Constraints
1 <= N <= 100000
-109 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return the maximum number of chunks that we could have made.



Example Input
 A = [2, 0, 1, 2]


Example Output
 2


Example Explanation
 We can split the array into two subarray one consisting element [2,0,1] and second one with only element [2].
 Sort them individually and concat them. The result will be sorted.

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        leftMaxArr = [A[0]]
        rightMinArr = [0]
        count = 1
        for i in range(1, len(A)):
            if leftMaxArr[i-1]<A[i]:
                leftMaxArr.append(A[i])
            else:
                leftMaxArr.append(leftMaxArr[i-1])
            rightMinArr.append(0)
        rightMinArr[len(A)-1] = A[len(A)-1]
        for i in range(len(A)-2, -1, -1):
            if A[i]<rightMinArr[i+1]:
                rightMinArr[i] = A[i]
            else:
                rightMinArr[i] = rightMinArr[i+1]
        for i in range(0,len(A)-1):
            if leftMaxArr[i]<=rightMinArr[i+1]:
                count+=1
        return count
