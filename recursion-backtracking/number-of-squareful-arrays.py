'''
Number of Squareful Arrays
Problem Description

Given an array of integers A, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Find and return the number of permutations of A that are squareful. Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].



Problem Constraints
1 <= length of the array <= 12

1 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return the number of permutations of A that are squareful.



Example Input
Input 1:

 A = [2, 2, 2]
Input 2:

 A = [1, 17, 8]


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 Only permutation is [2, 2, 2], the sum of adjacent element is 4 and 4 and both are perfect square.
Explanation 2:

 Permutation are [1, 8, 17] and [17, 8, 1].
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def permute(self,set1,set2,set3):
        if len(set1) == 0:#base
            set3.append([n for n in set2])
        seen_map = {}
        for i in range(0, len(set1)):
            if set1[i] in seen_map:
                continue
            else:
                seen_map[set1[i]] = 1
            new_set = []
            ele = set1[i]
            for j in range(0, len(set1)):
                if j!=i:
                    new_set.append(set1[j])
            set2.append(ele)
            if self.squareful(set2):
                self.permute(new_set,set2,set3)
            set2.pop()
        return set3
    def squareful(self,arr):
        flag = True
        for i in range(0, len(arr)-1):
            num = arr[i]+arr[i+1]
            if not num == ((int(num**0.5))**2):
                flag = False
                break
        return flag
    def solve(self, A):
        if len(A) == 1:
            return 0
        ans = self.permute(A,[],[])
        return len(ans)
        
