import sys
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
    original = b""
    with open(options["file"], "rb") as out:
        original = out.read()
    inp = b""
    if options["input"] == "":
        inp = input("message? ").encode('utf-8')
    else:
        with open(options["input"], "rb") as input_file:
            inp = input_file.read()
    start = -1
    for i in range(len(original)-2):
        if original[i+1] == 0xDA and original[i] == 0xFF:
            start = i+2
            break
    if start == -1:
        print("[stan] Does not seem to be a JPG or PNG file, moving on...")
    
    new = bytearray(original)
    for i in range(start, start+(len(inp)*8)):
        inpn = (i-start)//8
        bitn = (i-start)%8
        bit = (inp[inpn] >> bitn) & 1
        new[i] = (original[i] | bit) & bit
    with open("output.jpg", "wb") as out:
        out.write(bytes(new))

else:
    length = int(input("length? "))
    original = b""
    with open(options["file"], "rb") as out:
        original = out.read()
    start = -1
    for i in range(len(original)-2):
        if original[i+1] == 0xDA and original[i] == 0xFF:
            start = i+2

    message = bytearray()

    for i in range(start, start+length*8):
        if (i-start)%8 == 0:
            message.append(0)
        bit = original[i] & 1
        message[-1] = (message[-1] | (bit<<((i-start)%8)) )
    print(bytes(message))