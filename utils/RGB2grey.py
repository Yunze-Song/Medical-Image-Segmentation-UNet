from PIL import Image
import os

file_dir = 'C:/Users/Yunze/Desktop/Bladder_or/test/Images/'
out_dir = 'C:/Users/Yunze/Desktop/Bladder/test/Images/'
a = os.listdir(file_dir)

for i in a:
    print(i)
    I = Image.open(file_dir + i)
    L = I.convert('L')
    L.save(out_dir + i)
