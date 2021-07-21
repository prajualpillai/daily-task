import numpy as np
from scipy import linalg as lg


def solution(x,B,C):
    s = B.dot(C)
    a = [[1,1],[s[0][0],s[1][0]]]
    b = [[1],[x]]
    return((lg.solve(a,b).T).round(2))

n = int(input())
ans = []
for i in range(n):
    x = float(input())
    b = list(map(float,input().rstrip().split()))
    B = np.array([[b[0],b[1]],[b[2],b[3]]])
    c = list(map(float,input().rstrip().split()))
    C = np.array([[c[0]],[c[1]]])
    ans.append(solution(x,B,C))
for i in ans:
    print(*i)
