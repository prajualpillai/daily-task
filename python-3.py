class Increasinglist:
    def __init__(self):
        self.arr = list()
    def append(self,val):
        n = len(self.arr)
        if n > 0:            
            while self.arr[-1] > val and len(self.arr)>0:
                self.pop()            
        self.arr.append(val)
        #return self.arr
    def pop(self):
        self.arr.pop()
        #return self.arr
    def __len__(self):
        print(len(self.arr))
obj = Increasinglist()
N = int(input())
a = []
for i in range(N):
    q = list(input().rstrip().split())
    a.append(q)
for q in a:
    if q[0] == "size":
        obj.__len__()
    elif q[0] == "append":
        obj.append(q[1])
    elif q[0] == "pop":
        obj.pop()
    else:
        print("Input {} is invalid".format(i+1))
        