'''
Sieve of Eratosthenes
Count of divisors
Problem Description

Given an array of integers A, find and return the count of divisors of each element of the array.

NOTE: Order of the resultant array should be same as the input array.



Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 106



Input Format
The only argument given is the integer array A.



Output Format
Return the count of divisors of each element of the array in the form of an array.



Example Input
Input 1:

 A = [2, 3, 4, 5]
Input 2:

 A = [8, 9, 10]


Example Output
Output 1:

 [2, 2, 3, 2]
Output 1:

 [4, 3, 4]


Example Explanation
Explanation 1:

 The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
 So the count will be [2, 2, 3, 2].
Explanation 2:

 The number of divisors of 8 : [1, 2, 4, 8], 9 : [1, 3, 9], 10 : [1, 2, 5, 10]
 So the count will be [4, 3, 4].
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        mx, p = max(A), 2
        prime = [-1] * (mx+1) #Stores the smallest prime factor of integers 1 to max(A)
        while p*p <= mx:
            if prime[p] == -1:
                prime[p] = p
                for i in range(p*p, mx+1, p):
                    if prime[i] == -1:
                        prime[i] = p
            p += 1
        ans = []
        #Using prime factorization to get the number of divisors for every integer
        for i in A:
            if i == 1:
                ans.append(1)
                continue
            num, num_of_divisors = i, 1
            while num > 1:
                cnt = 0
                temp = prime[num]
                while num>1 and num%temp==0:
                    num //= temp
                    cnt += 1
                num_of_divisors *= (cnt+1)
            ans.append(num_of_divisors)
        return ans