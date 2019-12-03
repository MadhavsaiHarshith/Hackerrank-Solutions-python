if __name__ == '__main__':
    n = int(input())
    k =(input().split())
    p=[]
    for i in range(len(k)):
        p.append(int(k[i]))
    print(hash(tuple(p)))
    
