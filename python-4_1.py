import re
from sympy import Matrix,lcm
e = []
m = []
def elements(s):
    s1 = re.findall(('[A-Z][a-z]?'),s)
    for i in s1:
        if i not in e:
            e.append(i)
def mat(s,k,side):
  m.append([0]*len(e))
  s1 = re.findall(('[A-Z][a-z]?|\d+'),s)
  for i in range(len(s1)):
    try:
      if s1[i].isalpha() and s1[i+1].isnumeric():
        m[k][e.index(s1[i])] = int(s1[i+1])*side
      elif s1[i].isalpha():
        m[k][e.index(s1[i])] = 1*side
    except:
      if s1[i].isalpha():
        m[k][e.index(s1[i])] = 1*side



n = list(input().split('-'))
reac = n[0].split('+')
prod = n[1].split('+')

for i in reac:
    elements(i)

for i in range(len(reac)):
  mat(reac[i],i,1)
for j in range(len(prod)):
  i+=1
  mat(prod[j],i,-1)

m1 = Matrix(m)
m1 = m1.transpose()
sol = m1.nullspace()[0]
mul = lcm([val.q for val in sol])
print(*sol*mul)