import numpy as np
import matplotlib.pyplot as plt

path="C://OpenCv_Uygulamalar_1//src//smile.jpg"

img=plt.imread(path)#BGR
print(img)
print("Min value: ",img.min())
print("Min value: ",img.max())

#renklerin ortalaması bulunuyor.
print("mean: ",img.mean())

print("Median: ",np.median(img))

#Average:Ortalama
print("Average",np.average(img))
print("Mean1: ",img.max(img))