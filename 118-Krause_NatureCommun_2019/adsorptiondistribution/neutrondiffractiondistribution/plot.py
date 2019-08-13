import matplotlib.pyplot as plt
import numpy as np

Va = 0.06300000
Vb = 2.05800000
Vc = 7.90200000
Vd = 0.02200000

d = np.linspace(0,360,100)
print(d)

E = Va/2*(1+np.cos(d))+Vb/2*(1-np.cos(d))+Vc/2*(1+np.cos(d))+Vd/2*(1-np.cos(d))

print(E)

plt.plot(d,E)

plt.show()