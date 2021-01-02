'''
Bus and Passenger
There is bus having N rows, each row consist of two seats of equal size. Given an array A where A[i] determines the width of seats in the ith row.

There are 2*N passengers of type 0 and type 1 (exactly N passengers of type 0 and exactly N passengers of type 1).

Type 0 : Type 0 passenger always chooses a row where both seats are empty. Among these rows, he chooses the one with the smallest seat width and takes one of the seats in it.

Type 1 : Type 1 always chooses a row where exactly one seat is occupied (by a type 0 passenger). Among these rows, he chooses the one with the largest seat width and takes the vacant place in it.

You are given a string B determining the order the passenger entering the bus where B[i] is either '0' (type 0 passenger) or '1' (type 1 passenger).

Return an array of intergers C, where C[i] determines row taken by ith passenger.


Input Format

The argument given is the integer array A and string B.
Output Format

Return an array of integers C, where C[i] determines row taken by passenger i.
Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 10^5
length of string = 2 * length of array
B[i] is either '0' or '1'.
All array elements are distinct.
For Example

Input 1:
    A = [3, 1]
    B = "0011"
Output 1:
    C= [2, 1, 1, 2]

Input 2:
    A = [10, 8, 9, 11, 13, 5]
    B = "010010011101"
Output 2:
    C= [6, 6, 2, 3, 3, 1, 4, 4, 1, 2, 5, 5]
'''
class Solution:
    # @param A : list of integers
    # @param B : string
    # @return a list of integers
    def merge(self,A,l,mid,r):
        i = l
        j = mid+1
        temp = []
        while i <= mid and j <= r:
            if A[i][0] < A[j][0]:
                temp.append(A[i])
                i +=1
            else:
                temp.append(A[j])
                j +=1
        while i <= mid:
            temp.append(A[i])
            i +=1
        while j <= r:
            temp.append(A[j])
            j +=1
        k = 0
        for i in range(l,r+1):
            A[i] = temp[k]
            k+=1
    
    def mergeSort(self,A,l,r):
        if l < r:
            mid = int((l+r)/2)
            self.mergeSort(A,l,mid)
            self.mergeSort(A,mid+1,r)
            self.merge(A,l,mid,r)
    def solve(self, A, B):
        for i in range(0, len(A)):
            A[i] = [A[i],i+1]
        self.mergeSort(A,0,len(A)-1)
        ans = []
        stack = []
        top = 0
        for i in range(0, len(B)):
            if B[i] == "0":
                stack.append(A[top])
                ans.append(A[top][1])
                top += 1
            else:
                ele = stack.pop()
                ans.append(ele[1])
        return ans
