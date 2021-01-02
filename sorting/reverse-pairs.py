'''
Reverse pairs
Problem Description

Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j].
Return the number of important reverse pairs in the given array A.



Problem Constraints
1 <= length of the array <= 100000

1 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return the number of important reverse pairs in the given array A.



Example Input
Input 1:

 A = [1, 3, 2, 3, 1]
Input 2:

 A = [4, 1, 2]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 There are two pairs which are important reverse i.e (3, 1) and (3, 1).
Explanation 2:

 There is only one pair i.e (4, 1).
 '''
 class Solution:
    # @param A : list of integers
    # @return an integer
    def merge(self,A,l,mid,r):
        i = l
        j = mid+1
        count = 0
        ans = []
        while i <= mid and j <= r:
            if A[i]<A[j]:
                ans.append(A[i])
                i += 1
            else:
                ans.append(A[j])
                j += 1
        while i <= mid:
            ans.append(A[i])
            i += 1
        while j <= r:
            ans.append(A[j])
            j += 1
        i = l
        j = mid+1
        while i <= mid and j <= r:
            if A[i] > (2*A[j]):
                count += (mid-i+1)
                j+=1
            else:
                i += 1
        k = 0
        for m in range(l,r+1):
            A[m] = ans[k]
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
        return ans
