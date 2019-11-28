n=input().split()
m=input().split()
A,B=0,0
for i in range(len(n)):
    if int(n[i])>int(m[i]):
        A=A+1
    elif(int(n[i])==int(m[i])):
        pass
    elif(int(n[i])<int(m[i])):
        B=B+1
print(A,B)
