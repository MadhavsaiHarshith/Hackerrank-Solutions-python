
l=[]
z=[]
x=[]
y=[]
st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
count=0
count1=0
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
l.append(apples)
#print(l)
z.append(oranges)
#print(z)
for  i in range(len(apples)):
    x.append(abs(a+apples[i]))
for  i in range(len(oranges)):
    y.append(abs(b+oranges[i]))
#print(x)
#print(y)
for i in range(len(x)):
    if x[i] in range(s,t+1):
        count=count+1
   
for i in range(len(y)):
    if y[i] in range(s,t+1):
        count1=count1+1
    

print(count)    
print(count1)
