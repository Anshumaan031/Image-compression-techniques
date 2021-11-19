from PIL import Image 
import PIL 
  
# creating a image object (main image) 
im1 = Image.open(r"C:\Users\System-Pc\Desktop\flower1.jpg") 
  
# quantize a image 
im1 = im1.quantize(256) 
  
# to show specified image 
im1.show() 