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
        inp = input().encode('utf-8')
    else:
        with open(options["input"], "rb") as input_file:
            inp = input_file.read()
    start = -1
    for i in range(len(original)-2):
        if original[i+1] == 0xFF and original[i] == 0xDA:
            start = i+2
    if start == -1:
        print("[stan] Does not seem to be a JPG or PNG file, moving on...")
    
    new = bytearray(original)
    for i in range(start, start+(len(inp)*8)):
        new[i] = (original[i] | (inp[(i-start)//8] & (2**((i-start)%8)))) & ((inp[(i-start)//8] & (2**((i-start)%8)))  )
    with open("output.jpg", "wb") as out:
        out.write(bytes(new))

else:
    