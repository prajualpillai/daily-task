n = int(input())
a = []
if 1<= n <=1000: 
    for i in range(n):
        q = list(map(int,input().rstrip().split()))
        a.append(q)
    for q in a:
        try:
            s = q[0]*q[1]
            if s <= q[2]:
                print(s)
            else:
                print("multiplication of {} and {} with bound {} not possible".format(q[0],q[1],s))
        except ValueError:
            print("Invalid Input")
else:
    print("Invalid Input")