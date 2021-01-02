'''
Gcd Ordering
Given an array of integers A, find and return the lexicographically greatest arrangement of A which follows the below rules:

If the size of A is less than 3 it is always possible to rearrange A.

A[i] = A[i-1] + GCD(A[i-1], A[i-2]) for all i > 2, where GCD(x, y) is greatest common factor of x and y.

Return the lexicographically greatest arrangement of A which follows the above rules, if it is not possible to rearrange A according to the above rules return -1.

Note: Lexicographically means in dictionary order, i.e. if two arrangemnets are compared based on dictionary position the arrangements which comes afterwards is said to be Lexicographically greater.


Input Format

The only argument given is the integer array A.
Output Format

Return the lexicographically greatest arrangement of A  which follows the above rules, 
if it is not possible to rearrange A according to the given rules return -1.
Constraints

1 <= length of the array <= 100000
0 <= A[i] <= 10^5
For Example

Input 1:
    A = [4, 6, 2, 5, 3]
Output 1:
     [2, 3, 4, 5, 6]

Input 2:
    A = [3, 8, 5]
Output 2:
    -1
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def gcd(self,a,b):
        if a == 1 or b == 1:
            return 1
        if a == b:
            return a
        if a<b:
            a,b = b,a
        if b == 0:
            return a
        while b>0:
            a = a%b
            a,b = b,a
        return a
      
    def findlex(self,a, n): 
        flag = 0
        ans = [] 
        a.sort() 
        for i in range(2, n, 1): 
            if (a[i] != a[i - 1] + 
            self.gcd(a[i - 1], a[i - 2])): 
                flag = 1
                pos = i 
                break
        if (flag == 0): 
            if (a[1] == a[0] + 
            self.gcd(a[0], a[n - 1])): 
                ans.append(a[n - 1]) 
                for i in range(n - 1): 
                    ans.append(a[i]) 
      
                return ans
            else: 
                for i in range(n): 
                    ans.append(a[i]) 
      
                return ans
        else: 
            if (a[1] == a[0] + 
            self.gcd(a[pos], a[0])): 
                flag = 0
                i = n - 1
                while(i > pos + 2): 
                    if (a[i] != a[i - 1] + 
                    self.gcd(a[i - 1], a[i - 2])): 
                        flag = 1
                        break
                    i -= 1
                if (flag == 0 and pos < n - 1): 
                    if (a[pos + 1] != a[pos - 1] + 
                    self.gcd(a[pos - 1], a[pos - 2])): 
                        flag = 1
                if (flag == 0 and pos < n - 2): 
                    if (a[pos + 2] != a[pos + 1] +
                    self.gcd(a[pos - 1], a[pos + 1])): 
                        flag = 1
                if (flag == 0): 
                    ans.append(a[pos]) 
                    for i in range(n): 
                        if (i != pos): 
                            ans.append(a[i]) 
      
                    return ans
      
        ans.append(-1) 
        return ans
    def solve(self, A):
        ans = self.findlex(A,len(A))
        return ans
