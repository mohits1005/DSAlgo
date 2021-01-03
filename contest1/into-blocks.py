'''
Problem Description
A sequence of integers is called nice if its elements are arranged in blocks like in [3, 3, 3, 4, 1, 1]. Formally, if two elements are equal, everything in between must also be equal.
Let's define difficulty of a sequence as a minimum possible number of elements to change to get a nice sequence. However, if you change at least one element of value x to value y, you must also change all other elements of value x into y as well. For example, for [3, 3, 1, 3, 2, 1, 2] it isn't allowed to change first 1 to 3 and second 1 to 2. You need to leave 1's untouched or change them to the same value.
Print difficulty of given sequence A of size N.
Problem Constraints
1 <= N <= 200000
1 <= A[i] <= 200000
Input Format First and only argument of input is a single integer array A. Output Format Return a single integer denoting difficulty of A. Example Input Input 1: 
 A = [3, 7, 3, 7, 3] 
 Input 2: 
 A = [3, 3, 7, 7, 7, 1] 
 Input 3: 
 A = [3, 3, 1, 3, 2, 1, 2] 
Example Output Output 1: 
 2 
 Output 1: 
 0 
 Output 1: 
 4 
Example Explanation Explanation 1: 
 Change both 7 to 3. 
 Explanation 2: 
 No change required.
 '''
 class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        smap = {}
        for i in range(0,len(A)):
            if A[i] in smap:
                smap[A[i]][1] = i
            else:
                smap[A[i]] = [i,i]
        ranges = smap.values()
        ranges.sort()
        new_ranges = [ranges[0]]
        for i in range(1, len(ranges)):
            l1 = new_ranges[len(new_ranges)-1][0]
            r1 = new_ranges[len(new_ranges)-1][1]
            l2 = ranges[i][0]
            r2 = ranges[i][1]
            if l2 > r1:
                new_ranges.append(ranges[i])
            elif r1<r2:
                new_ranges[len(new_ranges)-1][1] = r2
        ans = 0
        for rangep in new_ranges:
            max = 0
            maxn = 0
            freq = {}
            for i in range(rangep[0],rangep[1]+1):
                if A[i] in freq:
                    freq[A[i]] += 1
                else:
                    freq[A[i]] = 1
                if freq[A[i]] > max:
                    max = freq[A[i]]
                    maxn = A[i]
            ans += (rangep[1]-rangep[0]+1-max)
        return ans
        
