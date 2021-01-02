'''
Ath Magical Number
Problem Description

Given three positive integers A, B and C.

Any positive integer is magical if it is divisible by either B or C.

Return the Ath magical number. Since the answer may be very large, return it modulo 109 + 7.



Problem Constraints
1 <= A <= 109

2 <= B, C <= 40000



Input Format
The first argument given is an integer A.

The second argument given is an integer B.

The third argument given is an integer C.



Output Format
Return the Ath magical number. Since the answer may be very large, return it modulo 109 + 7.



Example Input
Input 1:

 A = 1
 B = 2
 C = 3
Input 2:

 A = 4
 B = 2
 C = 3


Example Output
Output 1:

 2
Output 2:

 6


Example Explanation
Explanation 1:

 1st magical number is 2.
Explanation 2:

 First four magical numbers are 2, 3, 4, 6 so the 4th magical number is 6.
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def gcd(self,B,C):
        if C <= 0:
            return B
        else:
            return self.gcd(C,B%C)

    def lcm(self,B,C):
        return (B*C)/self.gcd(B,C)
        
    def solve(self, A, B, C):
        if B < C:
            B,C = C,B
        start = 1
        end = C*A
        lcm = self.lcm(B,C)
        while start < end:
            mid = int((start+end)/2)
            target = (mid/B)+(mid/C)-(mid/lcm)
            if target < A:
                start = mid + 1
            else:
                end = mid
        return end%(10**9+7)
