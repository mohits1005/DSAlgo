'''
Given an array of n integers, find the sum of f(a[i], a[j]) of all pairs (i, j) such that (1 <= i < j <= n).
f(a[i], a[j]):

If |a[j]-a[i]| > 1
   f(a[i], a[j]) = a[j] - a[i] 
Else // if |a[j]-a[i]| <= 1
   f(a[i], a[j]) = 0
Examples:

Input : 6 6 4 4 
Output : -8 
Explanation: 
All pairs are: (6 - 6) + (6 - 6) +
(6 - 6) + (4 - 6) + (4 - 6) + (4 - 6) + 
(4 - 6) + (4 - 4) + (4 - 4) = -8

Input: 1 2 3 1 3
Output: 4 
Explanation: the pairs that add up are:
(3, 1), (3, 1) to give 4, rest all pairs 
according to condition gives 0. 
'''
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def sum(self, A, B):
        sumpos = 0
        sumneg = 0
        for i in range(0,len(B)):
            sumpos += B[i]*i
            sumneg += B[i]*(len(B)-1-i)
        map = {}
        for i in range(0,len(B)):
            for j in range(B[i]-1,B[i]+2):
                if j in map:
                    sumpos -= map[j]*B[i]
            if B[i] in map:
                map[B[i]] += 1
            else:
                map[B[i]] = 1
        for i in range(0,len(B)):
            if B[i] in map:
                map[B[i]] -= 1
            for j in range(B[i]-1,B[i]+2):
                if j in map:
                    sumneg -= map[j]*B[i]
        return (sumpos-sumneg)%((10**9)+7)
        