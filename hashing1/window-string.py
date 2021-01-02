'''
Window String
Problem Description

Given a string A and a string B, find the window with minimum length in A which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in minimum window in A should be at least x.

Note:

If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index )


Problem Constraints
1 <= size(A), size(B) <= 106



Input Format
First argument is a string A.
Second argument is a string B.



Output Format
Return a string denoting the minimum window.



Example Input
Input 1:

 A = "ADOBECODEBANC"
 B = "ABC"
Input 2:

 A = "Aa91b"
 B = "ab"


Example Output
Output 1:

 "BANC"
Output 2:

 "a91b"


Example Explanation
Explanation 1:

 "BANC" is a substring of A which contains all characters of B.
Explanation 2:

 "a91b" is the substring of A which contains all characters of B.

'''
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        map = {}
        remain = 0
        for i in range(0, len(B)):
            if B[i] in map:
                map[B[i]] += 1
            else:
                map[B[i]] = 1
                remain += 1
        i = 0
        j = 0
        min = float('inf')
        ans = ""
        while i < len(A) or j < len(A):
            if remain == 0 and i < len(A):
                if j - i + 1 < min:
                    min = j - i + 1
                    ans = A[i:j]
                #window shrink
                if A[i] in map:
                    if map[A[i]] == 0:
                        remain += 1
                    map[A[i]] += 1 
                i += 1
            elif j < len(A):
                #window expand
                if A[j] in map:
                    if map[A[j]] == 1:
                        remain -= 1
                    map[A[j]] -= 1
                j += 1
            else:
                #either i len or j len
                break
        return ans
