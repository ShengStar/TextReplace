import os
import sys
arg1 = sys.argv[1]
rootdir = str(arg1)
list = os.listdir(rootdir)  
for i in range(0, len(list)):
    with open(os.path.join(rootdir, list[i]), 'r')as file:
        filedata = file.read()
        newdata = filedata.replace("reflectivity","intensity")
    with open(os.path.join(rootdir, list[i]), 'w')as file:
        file.write(newdata)

