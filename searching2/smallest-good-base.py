'''
Smallest Good Base
Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1. Now given a string representing A, you should return the smallest good base of A in string format.


Input Format

The only argument given is the string representing A.
Output Format

Return the smallest good base of A in string format.
Constraints

3 <= A <= 10^18
For Example

Input 1:
    A = "13"
Output 1:
    "3"     (13 in base 3 is 111)

Input 2:
    A = "4681"
Output 2:
    "8"     (4681 in base 8 is 11111).

×

'''
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = A
        n = int(n)
        max_len = len(bin(n)) - 2     # the longest possible representation "11111....1" based on k
        ans = -1
        for m in range(max_len, 1, -1):
            lo = 2
            hi = n - 1     # or hi = int(pow(n, pow(m - 1, -1))) and only need check hi
            while lo <= hi:
                mid = (lo + hi) / 2
                num = (pow(mid, m) - 1) // (mid - 1)
                if num < n:
                    lo = mid + 1
                elif num > n:
                    hi = mid - 1
                else:
                    ans = str(mid)
                    break
            if ans != -1:
                break
        return ans
