import sympy as sp
from sympy import *
from chempy import balance_stoichiometry as bs
rea,prod = bs({'NH4ClO4','Al'},{'Al2O3','HCl','H2O','N2'})
print(rea)
print(prod)