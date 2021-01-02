'''
Allocate Books
Problem Description

Given an array of integers A of size N and an integer B.

College library has N books,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.



NOTE: Return -1 if a valid assignment is not possible.



Problem Constraints
1 <= N <= 105
1 <= A[i], B <= 105



Input Format
The first argument given is the integer array A.
The second argument given is the integer B.



Output Format
Return that minimum possible number



Example Input
A = [12, 34, 67, 90]
B = 2


Example Output
113


Example Explanation
There are 2 number of students. Books can be distributed in following fashion : 
        1) [12] and [34, 67, 90]
        Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
        2) [12, 34] and [67, 90]
        Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
        3) [12, 34, 67] and [90]
        Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
        Of the 3 cases, Option 3 has the minimum pages = 113.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def validate(self,A,B,mid):
        painters = 1
        i = 0
        sum = 0
        result = 0
        while i<len(A):
            if sum + A[i] <= mid:
                sum += A[i]
            else:
                result = max(result, sum)
                sum = A[i]
                painters += 1
            i+=1
        if painters <= B:
            return [True, mid]
        else:
            return [False, mid]
    def books(self, A, B):
        start = 0
        end = 0
        ans = 0
        if len(A) < B:
            return -1
        for i in range(0, len(A)):
            if A[i]>start:
                start = A[i]
            end+=A[i]
        while start <= end:
            mid = int((start+end)/2)
            res = self.validate(A,B,mid)
            if res[0]:
                ans = res[1]
                end = mid - 1
            else:
                start = mid + 1
        return ans
