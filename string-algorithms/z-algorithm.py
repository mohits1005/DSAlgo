def bruteforceZ(S,Z):
    for i in range(0, len(S)):
        j = 0
        while i+j<len(S) and S[i+j] == S[j]:
            j+=1
        Z[i] = j

def findZ(S,Z):
    Z[0] = len(S)
    l = 0
    r = 0
    for i in range(1, len(S)):
        l = i
        r = i
        if i > r:
            #outside the window
            l,r = i,i
            while r < len(S) and S[r] == S[r-l]:
                r+=1
            Z[i] = r-l
            #one step extra
            r -= 1
        else:
            #inside the window
            k = i-l
            if Z[k]<r-i+1:
                #within bounds
                Z[i] = Z[k]
            else:
                #outside bounds
                l = i
                while r < len(S) and S[r] == S[r-l]:
                    r+=1
                Z[i] = r-l
                r -= 1


S = "xxyxxyxxaxxyxxz"
Z = [0 for i in range(0,len(S))]    
bruteforceZ(S,Z)
print(Z)
Z = [0 for i in range(0,len(S))]    
findZ(S,Z)
print(Z)
