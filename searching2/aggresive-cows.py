'''
Aggressive cows
Problem Description

Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?



Problem Constraints
2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N



Input Format
The first argument given is the integer array A.
The second argument given is the integer B.



Output Format
Return the largest minimum distance possible among the cows.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 
John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
So the minimum distance will be 2.
Explanation 2:

 
The minimum distance will be 1.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def validate(self,mid, C, A):
        possible = True
        i = 1
        while i < len(A) and C > 0:
            if A[i]-A[i-1] < mid:
                prev = A[i-1]
                while A[i]-prev < mid:
                    if i == len(A)-1:
                        break
                    i+=1
                if A[i]-prev < mid:
                    possible = False
                    break
                i += 1
            else:
                i += 1
            C -= 1
        if C > 0:
            return False
        return possible
    def solve(self, A, B):
        start = 1
        A.sort()
        end = A[len(A)-1]-A[0]
        C = B - 1
        ans = 0
        while start <= end:
            mid = int((start+end))/2
            flag = self.validate(mid, C, A)
            if flag:
                if mid > ans:
                    ans = mid
                start = mid+1
            else:
                end = mid - 1
        return ans
