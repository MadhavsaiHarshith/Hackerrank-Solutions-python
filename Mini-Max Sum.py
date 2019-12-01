def miniMaxSum(arr):
    c=[]
    for i in range(len(arr)):
        g=arr.pop()
        c.append(sum(arr))
        arr.insert(0,g)
    print(min(c),max(c))
