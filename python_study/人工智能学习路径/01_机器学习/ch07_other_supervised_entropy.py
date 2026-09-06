import numpy as np
import matplotlib.pyplot as plt
p=np.arange(0.01,1,0.01)
H=-p*np.log2(p)-(1-p)*np.log2(1-p)
plt.plot(p,H)
plt.xlabel('p')
plt.ylabel('H')
plt.show()