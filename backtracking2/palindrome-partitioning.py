'''
Palindrome Partitioning
Problem Description

Given a string A, partition A such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of A.

Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
(len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))


Problem Constraints
1 <= len(A) <= 15



Input Format
First argument is a string A of lowercase characters.



Output Format
Return a list of all possible palindrome partitioning of s.



Example Input
Input 1:

A = "aab"
Input 2:

A = "a"


Example Output
Output 1:

 [
    ["a","a","b"]
    ["aa","b"],
  ]
Output 2:

 [
    ["a"]
  ]


Example Explanation
Explanation 1:

In the given example, ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa").
Explanation 2:

In the given example, only partition possible is "a" .

'''
class Solution:
    # @param A : string
    # @return a list of list of strings
    def isPalindrome(self,string):
        newString = ""
        for i in range(len(string)-1,-1,-1):
            newString+=string[i]
        return string == newString
    def recc(self,string,arr,answer):
        if len(string) == 0:
            answer.append([x for x in arr])
            return
        i = 0
        while i < len(string):
            prefix = string[:i+1]
            res = string[i+1:]
            if self.isPalindrome(prefix):
                tempArr = arr
                tempArr.append(prefix)
                self.recc(res,tempArr,answer)
                tempArr.pop()
            i+= 1
    def partition(self, A):
        ans = []
        self.recc(A,[],ans)
        return ans
        
