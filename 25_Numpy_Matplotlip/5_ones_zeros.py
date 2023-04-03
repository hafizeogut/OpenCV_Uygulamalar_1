import numpy as np

x=np.empty([3,3],np.uint8)
print(x)
print("----------")

#dolu bir dizi oluşturuluyor.
y=np.full((3,3,3),dtype=np.int16,fill_value=5)
print(y)
print("----------")

z=np.ones((2,5,5),dtype=np.int8)
print(z)

z=np.zeros((2,5,5),dtype=np.int8)
print(z)