'''
Single Number III
Problem Description

Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Note: Output array must be sorted.



Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109



Input Format
First argument is an array of interger of size N.



Output Format
Return an array of two integers that appear only once.



Example Input
Input 1:

A = [1, 2, 3, 1, 2, 4]
Input 2:

A = [1, 2]


Example Output
Output 1:

[3, 4]
Output 2:

[1, 2]


Example Explanation
Explanation 1:

 3 and 4 appear only once.
Explanation 2:

 1 and 2 appear only once.
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        xor = 0
        for x in A:
            xor = xor ^ x
        i = 0
        while i <= 31:
            if xor & (1 << i):
                break
            i+=1
        i = 1 << i
        first = 0
        second = 0
        for num in A:
            if num & i:
                first = first^num
            else:
                second = second^num
        if first < second:
            first, second = second, first
        return [second, first]
