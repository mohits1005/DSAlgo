'''
Permutations of A in B
Problem Description

You are given two strings A and B of size N and M respectively.

You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.



Problem Constraints
1 <= N < M <= 105



Input Format
Given two argument, A and B of type String.



Output Format
Return a single Integer, i.e number of permutations of A present in B as a substring.



Example Input
Input 1:

 A = "abc"
 B = "abcbacabc"
Input 2:

 A = "aca"
 B = "acaa"


Example Output
Output 1:

 5
Output 2:

 2


Example Explanation
Explanation 1:

 Permutations of A that are present in B as substring are:
    1. abc
    2. cba
    3. bac
    4. cab
    5. abc
    So ans is 5.
Explanation 2:

 Permutations of A that are present in B as substring are:
    1. aca
    2. caa 
    '''
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        map = {}
        remaining = 0
        count = 0
        for i in range(0, len(A)):
            if A[i] in map:
                map[A[i]] += 1
            else:
                map[A[i]] = 1
                remaining += 1
        i,j = 0,0
        while i < len(B) and j < len(B):
            if map[B[j]] > 0:
                #expand
                if map[B[j]] == 1:
                    remaining -= 1
                map[B[j]] -= 1
                j += 1
            elif B[j] in map:
                #shrink
                if map[B[i]] == 0:
                    remaining += 1
                map[B[i]] += 1
                i+=1
            else:
                while i < j:
                    if map[B[i]] == 0:
                        remaining += 1
                    map[B[i]] += 1
                    i+=1
                i+=1
                j+=1
            if remaining == 0:
                count += 1
        return count
