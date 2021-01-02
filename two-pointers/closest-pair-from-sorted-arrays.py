'''
Closest pair from sorted arrays
Problem Description

Given two sorted arrays of distinct integers, A and B, and an integer C, find and return the pair whose sum is closest to C and the pair has one element from each array.

More formally, find A[i] and B[j] such that abs((A[i] + B[j]) - C) has minimum value.

If there are multiple solutions find the one with minimum i and even if there are multiple values of j for the same i then return the one with minimum j.

Return an array with two elements {A[i], B[j]}.



Problem Constraints
1 <= length of both the arrays <= 100000

1 <= A[i], B[i] <= 109

1 <= C <= 109



Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.
The third argument given is integer C.



Output Format
Return an array of size 2 denoting the pair which has sum closest to C.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
 B = [2, 4, 6, 8]
 C = 9
Input 2:

 A = [5, 10, 20]
 B = [1, 2, 30]
 C = 13


Example Output
Output 1:

 [1, 8]
Output 2:

 [10, 2]


Example Explanation
Explanation 1:

 There are three pairs: (1, 8), (3, 6), (5, 4), that gives the minimum value.
 Since we have to return the value with minimum i and then with minimum j. We will return [1, 8].
Explanation 2:

 [10, 2] is the only pair such abs(10+2-13) is minimum.
 '''
 class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        i = 0
        j = len(B)-1
        ans = float('inf')
        oldans = -1
        pairs = set()
        while i < len(A) and j >= 0:
            if abs(A[i]+B[j]-C) <= ans:
                oldans = ans
                ans = abs(A[i]+B[j]-C)
                if oldans != ans:
                    pairs = set()
                pairs.add((A[i],B[j]))
            if A[i]+B[j] < C:
                i+=1
            elif A[i]+B[j]>C:
                j-=1
            else:
                i += 1
                j -= 1
        mini = float('inf')
        minj = float('inf')
        for ele in pairs:
            if ele[0] < mini:
                mini = ele[0]
                minj = ele[1]
            elif ele[0] == mini:
                if ele[1] < minj:
                    minj = ele[1]
        ans = [mini,minj]
        return ans
