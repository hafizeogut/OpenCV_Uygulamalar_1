import numpy as np
import matplotlib.pyplot as plt

x=np.arange(3)
plt.plot(x,[y**2  for y in x])

plt.plot(x,[y**3 for y in x])
plt.plot(x,2*x)
plt.plot(x,5.2*x)

#hangi deeğer hangi grafiğe ait tespit ediliyor.
plt.legend(["x**2","x**3","2*x","x*5.2"],loc="upper center")#upper right/center/left,lower right/center/left


#Izgara oluşturuluyor
plt.grid(True)


print(plt.axis()) 


#Eksenin max ve min noktaları ayarlanıyor.
plt.axis([0,2,0,10])


plt.title("Simple Plot")
plt.xlabel("x = np.arange(3)")
plt.ylabel("y = np.arange(3)")
plt.savefig("C://OpenCv_Uygulamalar_1//output//asd.png")
plt.show()
