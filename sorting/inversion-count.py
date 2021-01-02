'''
Inversion count in an array
Problem Description

Given an array of integers A. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).



Problem Constraints
1 <= length of the array <= 100000

1 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return the number of inversions of A modulo (109 + 7).



Example Input
Input 1:

A = [3, 2, 1]
Input 2:

A = [1, 2, 3]


Example Output
Output 1:

3
Output 2:

0


Example Explanation
Explanation 1:

 All pairs are inversions.
Explanation 2:

 No inversions.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def merge(self,A,l,mid,r):
        i = l
        j = mid+1
        count = 0
        arr = []
        while i <= mid and j <= r:
            if A[i] <= A[j]:
                arr.append(A[i])
                i += 1
            else:
                count += mid - i + 1
                arr.append(A[j])
                j += 1
        while i <= mid:
            arr.append(A[i])
            i += 1
        while j <= r:
            arr.append(A[j])
            j += 1
        k = 0
        for i in range(l,r+1):
            A[i] = arr[k]
            k += 1
        return count

    def mergeSort(self,A,l,r):
        count = 0
        if l < r:
            mid = int((l+r)/2)
            count += self.mergeSort(A,l,mid)
            count += self.mergeSort(A,mid+1,r)
            count += self.merge(A,l,mid,r)
        return count
    def solve(self, A):
        ans = self.mergeSort(A,0,len(A)-1)
        return ans%(10**9+7)
        
