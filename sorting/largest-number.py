'''
Largest Number
Problem Description

Given a array A of non negative integers, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.



Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109



Input Format
First argument is an array of integers.



Output Format
Return a string representing the largest number.



Example Input
Input 1:

 A = [3, 30, 34, 5, 9]
Input 2:

 A = [2, 3, 9, 0]


Example Output
Output 1:

 "9534330"
Output 2:

 "9320"


Example Explanation
Explanation 1:

 A = [3, 30, 34, 5, 9]
 Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
Explanation 2:

 Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320. 
 '''
 class Solution:
    # @param A : tuple of integers
    # @return a strings
    def merge(self,A,l,mid,r):
        temp = []
        i = l
        j = mid+1
        while i <= mid and j <= r:
            if str(A[i])+str(A[j]) > str(A[j])+str(A[i]):
                temp.append(A[i])
                i+=1
            else:
                temp.append(A[j])
                j+=1
        while i <= mid:
                temp.append(A[i])
                i+=1
        while j <= r:
                temp.append(A[j])
                j+=1
        k = 0
        for i in range(l,r+1):
            A[i] = temp[k]
            k+=1
    def mergeSort(self,A,l,r):
        if l == r:
            return
        mid = int((l+r)/2)
        self.mergeSort(A,l,mid)
        self.mergeSort(A,mid+1,r)
        self.merge(A,l,mid,r)
            
    def largestNumber(self, A):
        A = list(A)
        self.mergeSort(A,0,len(A)-1)
        string = ""
        for i in range(0, len(A)):
            string += str(A[i])
        if string[0] == '0':
            return '0'
        return string
