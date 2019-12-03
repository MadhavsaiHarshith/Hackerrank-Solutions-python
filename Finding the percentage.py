import math
n = int(input())
student_marks = {}

p=[]
for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        s=sum(scores)
        p=len(scores)
        g=float(s/p)
        student_marks[name]=g
q=input()
        
l=student_marks[q]
print("{0:.2f}".format(l))
