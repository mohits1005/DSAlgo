'''
Generate all Parentheses II
Problem Description

Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.



Problem Constraints
1 <= A <= 20



Input Format
First and only argument is integer A.



Output Format
Return a sorted list of all possible paranthesis.



Example Input
Input 1:

A = 3
Input 2:

A = 1


Example Output
Output 1:

[ "((()))", "(()())", "(())()", "()(())", "()()()" ]
Output 2:

[ "()" ]


Example Explanation
Explanation 1:

 All paranthesis are given in the output list.
Explanation 2:

 All paranthesis are given in the output list.
'''
class Solution:
    # @param A : integer
    # @return a list of strings
    def recc(self,A,str,left,right,ans):
        if len(str) == 2*A:
            ans.append(str)
            return
        if left < A:
            self.recc(A,str+'(',left+1,right,ans)
        if right < left:
            self.recc(A,str+')',left+1,right,ans)
    def generateParenthesis(self, A):
        ans = []
        self.recc(A,"",0,0,ans)
        return ans
