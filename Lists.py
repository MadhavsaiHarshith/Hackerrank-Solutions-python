if __name__ == '__main__':
    N = int(input())
l=[]
for i in range(N):
    s=input().split()
    cmd=s[0]
    arg=s[1:]
    
    if(cmd=="print"):
        print(l)
    else:
        cmd=cmd+"("+",".join(arg)+")"
        eval("l."+cmd)
