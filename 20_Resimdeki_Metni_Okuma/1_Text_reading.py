from PIL import Image
import pytesseract

img=Image.open("C://OpenCv_Uygulamalar_1//src//text.png")
text=pytesseract.image_to_string(img,lang="eng")
print(text)