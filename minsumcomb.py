from argminsum import argminsum, min, zero, inf

def minsumcomb(x:list,M:int):

    N=len(x)
    S=[[zero]+[inf]*M]
    X=[argminsum(i,[i]) for i in x]

    for n in range(1,N+1):
        a=[zero]
        for m in range(1,M+1):
            a.append(min(S[n-1][m], argminsum.__add__(S[n-1][m-1], X[n-1])))
        S.append(a)

    return S


print(minsumcomb([11,3,-5,8,2,-2,-4,1],3))