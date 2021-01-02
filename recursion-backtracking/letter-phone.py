'''
Letter Phone
Problem Description

Given a digit string A, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself. The digit 1 maps to 1 itself.

NOTE: Make sure the returned strings are lexicographically sorted.



Problem Constraints
1 <= |A| <= 10



Input Format
The only argument is a digit string A.



Output Format
Return a string array denoting the possible letter combinations.



Example Input
Input 1:

 A = "23"
Input 2:

 A = "012"


Example Output
Output 1:

 ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Output 2:

 ["01a", "01b", "01c"]


Example Explanation
Explanation 1:

 There are 9 possible letter combinations.
Explanation 2:

 Only 3 possible letter combinations.
'''
class Solution:
    # @param A : string
    # @return a list of strings
    def recc(self,A, arr, index):
        obj = {
        "0":"0",
        "1":"1",
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}
        if index == len(A):
            return arr
        else:
            tempArr = []
            if index == 0:
                j = 0
                while j<len(obj[A[index]]):
                    tempArr.append(obj[A[index]][j])
                    j += 1
            else:
                    for i in range(0, len(arr)):
                        j = 0
                        while j<len(obj[A[index]]):
                            tempArr.append(arr[i]+obj[A[index]][j])
                            j += 1
            return self.recc(A, tempArr, index+1)
    def letterCombinations(self, A):
        ans = self.recc(A,[], 0)
        return ans
