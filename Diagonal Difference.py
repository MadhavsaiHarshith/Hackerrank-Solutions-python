n=int(input())
c=[]
for i in range(n):
    v=list(map(int,input().split()))
    c.append(v)
sum1=0
sum=0
j=n-1
for i in range(n):
    sum=c[i][i]+sum
    sum1=c[i][j]+sum1
    j=j-1
print(abs(sum1-sum))    
