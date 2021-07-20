def multiply(a,b,bound):
    try:
        s = a*b
        if s <= bound:
            print(s)
        else:
            print("multiplication of {} and {} with bound {} not possible".format(a,b,bound))
    except ValueError:
        print("Invalid Input")



n = int(input())
a = []
if 1<= n <=1000: 
    for i in range(n):
        q = list(map(int,input().rstrip().split()))
        a.append(q)
    for q in a:
        multiply(q[0],q[1],q[2])
        
else:
    print("Invalid Input")
    print("test")