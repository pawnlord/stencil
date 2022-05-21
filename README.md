# stencil
Stenography program for adding data into images  
Currently only tested with JPEGs and PNGs

## usage
```
[python3] stencil.py <input_image> [-d(ecrypt)] [-i <input_text>] [-o <output_image>]
```
While images can be either PNGs or JPEGs, the output needs to be a PNG in order to have lossless compression.  
`-o` is expected after `-d` when decrypting, if you want to output the result to a file  

## dependencies
Currently, stencil requires NumPy and Pillow to run   