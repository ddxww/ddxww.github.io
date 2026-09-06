import pulp
from pulp import value
import numpy as np
z=[2,3,1]
a=[
    [1,4,2],
    [3,2,0]
]
b=[8,6]
m=pulp.LpProblem("My Problem", pulp.LpMinimize)
x=[pulp.LpVariable(f"x{i}",lowBound=0)for i in [1,2,3]]
m+=pulp.lpDot(z,x)
for i in range(len(a)):
    m+=pulp.lpDot(a[i],x)>=b[i]
m.solve()
items = [value(x[i]) for i in range(3)]
print(pulp.value(m.objective))
print(items)
items_np = np.array(items)
print(items_np.astype(int))

