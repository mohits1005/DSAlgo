'''
Remove Invalid Parentheses
Problem Description

Given a string A consisting of lowercase English alphabets and parentheses '(' and ')'. Remove the minimum number of invalid parentheses in order to make the input string valid.

Return all possible results.

You can return the results in any order.



Problem Constraints
1 <= length of the string <= 20



Input Format
The only argument given is string A.



Output Format
Return all possible strings after removing the minimum number of invalid parentheses.



Example Input
Input 1:

 A = "()())()"
Input 2:

 A = "(a)())()"


Example Output
Output 1:

 ["()()()", "(())()"]
Output 2:

 ["(a)()()", "(a())()"]


Example Explanation
Explanation 1:

 By removing 1 parentheses we can make the string valid.
        1. Remove the parentheses at index 4 then string becomes : "()()()"
        2. Remove the parentheses at index 2 then string becomes : "(())()"
Explanation 2:

 By removing 1 parentheses we can make the string valid.
        1. Remove the parentheses at index 5 then string becomes : "(a)()()"
        2. Remove the parentheses at index 2 then string becomes : "(a())()"
'''
class Solution:
    # @param A : string
    # @return a list of strings
    def isValid(self,exp):
        left = 0
        right = 0
        flag = True
        i = 0
        while i < len(exp):
            if exp[i] == '(':
                left += 1
            if exp[i] == ')':
                right += 1
            if right > left:
                flag = False
                break
            i+=1
        return flag
    def recc(self,A, index, l, r, exp,ans):
        if index == len(A):
            if l == 0 and r == 0:
                if exp not in ans:
                    ans.append(exp)
            return
        if A[index] == '(':
            if l > 0:
                self.recc(A, index+1, l-1, r, exp,ans)
            self.recc(A,index+1, l, r, exp+"(",ans)
        elif A[index] == ')':
            if r > 0:
                self.recc(A, index+1, l, r-1, exp,ans)
            if self.isValid(exp+")"):
                self.recc(A,index+1, l, r, exp+")",ans)
        else:
            self.recc(A,index+1, l, r, exp+A[index],ans)
    def solve(self, A):
        l, r = 0, 0
        for i in range(0,len(A)):
            if A[i] == '(':
                l += 1
            elif A[i] == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1   
        ans = []
        self.recc(A,0,l,r,"",ans)
