def plusMinus(arr):
    count=0
    count1=0
    c=0
    for i in range(len(arr)):
        if(arr[i]>0):
            count=count+1
        if(arr[i]<0):
            count1=count1+1
        if(arr[i]==0):
            c=c+1
    print(count/len(arr))
    print(count1/len(arr))
    print(c/len(arr))
