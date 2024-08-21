



fh = open("output.bin", "rb")

stuff = fh.read()

fh.close()

print(stuff.hex())


