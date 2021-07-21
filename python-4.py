import sympy as sp
from sympy import *
p,q,r,s,t,u = symbols('p,q,r,s,t,u')
for i in range(50):
    ans = solve((p-2*u,4*p-s-2*t,p-s,4*p-3*r-t,q-2*r,p-i),p,q,r,s,t,u)
    if all(type(j)==sp.core.numbers.Integer for j in ans.values()):
        print(ans)
        break