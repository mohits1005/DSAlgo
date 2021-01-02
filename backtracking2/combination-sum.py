'''
Combination Sum
Problem Description

Given a set of candidate numbers A and a target number B, find all unique combinations in A where the candidate numbers sums to B.

The same repeated number may be chosen from A unlimited number of times.

Note:

1) All numbers (including target) will be positive integers.

2) Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).

3) The combinations themselves must be sorted in ascending order.

4) CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR ... (a1 = b1 AND a2 = b2 AND ... ai = bi AND ai+1 > bi+1)

5) The solution set must not contain duplicate combinations.



Problem Constraints
1 <= |A| <= 20

1 <= A[i] <= 50

1 <= B <= 500



Input Format
First argument is the vector A.

Second argument is the integer B.



Output Format
Return a vector of all combinations that sum up to B.



Example Input
Input 1:

A = [2, 3]
B = 2
Input 2:

A = [2, 3, 6, 7]
B = 7


Example Output
Output 1:

[ [2] ]
Output 2:

[ [2, 2, 3] , [7] ]


Example Explanation
Explanation 1:

All possible combinations are listed.
Explanation 2:

All possible combinations are listed.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def recc(self,A,B,arr,index,sum,ans):
        #check running sum
        if sum == B:
            ans.insert(0,[x for x in arr])
            return
        #base condition
        if index == len(A):
            return
        #recurse all occurences of index
        occurence = 0
        while sum+A[index]*occurence <= B:
            temp = occurence
            while temp > 0:
                arr.append(A[index])
                sum += A[index]
                temp -= 1
            self.recc(A,B,arr,index+1,sum,ans)
            #reset
            temp = occurence
            while temp > 0:
                arr.pop()
                sum -= A[index]
                temp -= 1
            occurence += 1
    def combinationSum(self, A, B):
        A.sort()
        ans = []
        self.recc(A,B,[],0,0,ans)
        return ans
        
