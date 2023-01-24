import numpy as np

n = 87

left = []
right = []
for i in range(n):
    n1 = n-i
    n2 = n+i
    mods1 = [ n1%i for i in range(2,n1//2+1) ]
    mods2 = [ n2%i for i in range(2,n2//2+1) ]
    left.append((n1,mods1))
    right.append((n2,mods2))
    if mods1.count(0) == mods2.count(0) and mods1.count(0) == 0:
        print(i)
        break

for l in left:
    print(l[0], end=' | ')
    print([ f"{x:2}" for x in l[1]])

print("--"*20)

for r in right:
    print(r[0], end=' | ')
    print([ f"{x:2}" for x in r[1]])

print("--"*20)

print(f"{n1} + {n2} = {2*n}")
