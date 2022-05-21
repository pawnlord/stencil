import sys
import PIL as pil
from PIL import Image
from PIL import ImageMode
import numpy as np

options = {"file":"", "encrypt":True, "input":""}

for o in range(1,len(sys.argv)):
    if sys.argv[o] == "-d":
        options["encrypt"] = False
    elif sys.argv[o] == "-i":
        if len(sys.argv) == o+1 or sys.argv[o+1][0] == '-':
            print("[stan] Input implied, but none given")
            exit()
        options["input"] = sys.argv[o+1]
    else:
        options["file"] = sys.argv[o]
    
if options["file"] == "":
    print("[stan] No file given, exiting")
    exit()


if options["encrypt"]:
    im = pil.Image.open(options["file"])
    original = list(im.getdata())

    width, height = im.size
    im.close()
    inp = b""

    if options["input"] == "":
        inp = input("message? ").encode('utf-8')
    else:
        with open(options["input"], "rb") as input_file:
            inp = input_file.read()

    new = [list(t) for t in original]
    for i in range(0, len(inp)*8):
        inpn = (i)//8
        bitn = (i)%8
        bit = (inp[inpn] >> bitn) & 1
        pixel = i//3
        value = i%3
        new[pixel][value] = (original[pixel][value] | bit) & bit

    formatted_new = [] #[[tuple(new[(i*im.height) + j]) for j in range(im.height) ] for i in range(im.width)]
    for i in range(height):
        formatted_new.append([])
        for j in range(width):
            formatted_new[i].append(tuple(new[(i*width) + j]))
    # format array

    final = np.asarray(formatted_new, dtype=np.uint8)
    im = pil.Image.fromarray(final)
    im.save("output.png")
else:
    length = int(input("length? "))
    im = pil.Image.open(options["file"])
    original = list(im.getdata())
    data = []
    for i in range(length*8):
        if i%8 == 0:
            data.append(0)
        pixel = i//3
        value = i%3
        bit = ((original[pixel][value] & 1) << i%8) 
        data[-1] = (data[-1] | bit) 
    print(bytes(data))
        
