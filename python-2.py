def even(start,n):
    if start%2 != 0:
        start+=1

    for i in range(n):
        print(start+2*i, end = " ")

m = list(map(int,input().rstrip().split()))
even(m[0],m[1])