f=list(map(int,input().split()))
i=f[0]
j=f[1]
k=f[2]
l=f[3]
c,d=[],[]
for n in range(f[0]+20*15):
    i=i+j
    k=k+l
    c.append(i)
    d.append(k)
    #print(i,k)
e=0
for i in range(len(d)):
    if c[i]==d[i]:
        e=e+1
        #print("yes")
    else:
       # print("No")
        e=e

if e==1:
    print("YES")
else:
    print("NO")
