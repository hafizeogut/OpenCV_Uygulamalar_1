import numpy as np
import matplotlib.pyplot as plt


#girilen aralık veri üretiliyor.
N=11
x=np.linspace(0,10,N)
print(x)
y=x

plt.plot(x,y,"o--")
plt.axis("off")


plt.show()

x=[3,0,7,1,8,4,4,6,4]
plt.plot(x)
plt.show()


plt.plot(x,[y**2 for y in x])
plt.show()