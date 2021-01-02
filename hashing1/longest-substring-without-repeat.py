'''
Longest Substring Without Repeat
Problem Description

Given a string A, find the length of the longest substring without repeating characters.

Note: Users are expected to solve in O(N) time complexity.



Problem Constraints
1 <= size(A) <= 106

String consists of lowerCase,upperCase characters and digits are also present in the string A.



Input Format
Single Argument representing string A.



Output Format
Return an integer denoting the maximum possible length of substring without repeating characters.



Example Input
Input 1:

 A = "abcabcbb"
Input 2:

 A = "AaaA"


Example Output
Output 1:

 3
Output 2:

 2


Example Explanation
Explanation 1:

 Substring "abc" is the longest substring without repeating characters in string A.
Explanation 2:

 Substring "Aa" or "aA" is the longest substring without repeating characters in string A.
 '''
 class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        map = {}
        i,j = 0,0
        ans = 0
        while i < len(A) and j < len(A):
            if A[j] in map:
                #shrink
                k = map[A[j]]
                while i <= k:
                    del map[A[i]]
                    i += 1
            else:
                #expand
                map[A[j]] = j
                ans = max(ans,j-i+1)
                j+=1
        return ans
