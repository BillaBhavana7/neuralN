L1=list(map(float,input().split()))
L2=[]
for x in L1:
    x=x*2.54
    L2.append(x)
print(L2)

L1=list(map(float,input().split()))
L2=[x*2.54 for x in L1]
print(L2)