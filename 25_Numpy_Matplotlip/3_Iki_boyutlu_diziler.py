import numpy as np

xy=np.array([[3,0,7],[4,5,6],[4,6,4]],np.int16)#çok boyutlu dizi
print(xy)
print("------------------")
x=np.array([[3,0,7],[4,5,6]],np.int16)
print(x[0])
print(x[0,0])
print(x[0][1])

print("---------")
print(x[:,0])#3ve 4

print("---------")
print(x[:,1])#0ve 5

print("---------")
print(x[:,2])#7 ve 6

print("---------")
print(x[0,:])

print("---------")
print(x[1,:])