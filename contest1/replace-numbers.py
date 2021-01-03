'''
Problem DescriptionYou have an array A of length N. You are asked to perform Q queries on the array. In ith operation, you have to replace all the occurrences of B[i][0] with some B[i][1].
Find the final array after doing all the operations sequentially.

Problem Constraints1 <= N, Q <= 2 x 105
1 <= A[i], B[i][0], B[i][1] <= 50

Input FormatThe first argument contains the integer array A.
The second argument contains the queries B.

Output FormatReturn the final array after performing operations sequentially.Example Input
  Input 1:

  A : [ 2, 2, 5, 1 ]
  B : 
  [
    [2, 4]
    [5, 2]
  ]

Input 2:

  A : [ 5, 1, 3, 1 ]
  B : 
  [
    [1, 5]
    [5, 3]
  ]

Example Output
  Output 1:

  [4, 4, 2, 1]

Output 2:

  [3, 3, 3, 3]

Example Explanation
  Explanation 1:

  After first operation the array becomes, [4, 4, 5, 1].
  After second operation the array becomes [4, 4, 2, 1]

Explanation 2:

  After first operation the array becomes, [5, 5, 3, 5].
  After second operation the array becomes [3, 3, 3, 3]

        
          ×
          -->
            
              
              
              
            
          
          You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.
          '''
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        C = [ i for i in range(0,51)]
        for op in B:
            for j in range(0, len(C)):
                if C[j] == op[0]:
                    C[j] = op[1]
        for i in range(0, len(A)):
            A[i] = C[A[i]]
        return A
