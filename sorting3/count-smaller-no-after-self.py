'''
Count of smaller numbers after self
Problem Description

Given an array of integers A, find and return new integer array B.

Array B has the property where B[i] is the number of smaller elements to the right of A[i].



Problem Constraints
1 <= length of the array <= 100000

1 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return the new integer array B.



Example Input
A = [1, 5, 4, 2, 1]


Example Output
[0, 3, 2, 1, 0]


Example Explanation
Number of smaller elements to the right of 1 are 0.
Number of smaller elements to the right of 5 are 3 (4, 2, 1).
Number of smaller elements to the right of 4 are 2 (2, 1).
Number of smaller elements to the right of 2 are 1 (1).
Number of smaller elements to the right of 1 are 0.
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def merge(self,A,l,mid,r,ans):
        i = l
        j = mid+1
        temp = []
        smallRightCounter = 0
        while i <= mid and j <= r:
            if A[i][0] <= A[j][0]:
                ans[A[i][1]] += smallRightCounter
                temp.append(A[i])
                i += 1
            else:
                smallRightCounter += 1
                temp.append(A[j])
                j += 1
        while i <= mid:
            ans[A[i][1]] += smallRightCounter
            temp.append(A[i])
            i += 1
        while j <= r:
            temp.append(A[j])
            j += 1
        k = 0
        for i in range(l,r+1):
            A[i] = temp[k]
            k += 1
    def mergeSort(self,A,l,r,ans):
        if l < r:
            mid = int((l+r)/2)
            self.mergeSort(A,l,mid,ans)
            self.mergeSort(A,mid+1,r,ans)
            self.merge(A,l,mid,r,ans)
    def solve(self, A):
        for i in range(0, len(A)):
            A[i] = [A[i],i]
        ans = [0 for x in range(0, len(A))]
        self.mergeSort(A,0,len(A)-1,ans)
        return ans
