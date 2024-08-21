#!/bin/sh







if __name__=="__main__":

	fh = open("test_program.py", "r")
	lines = fh.readlines()

	fh.close()

	split_string = ".fromhex(\""

	thing = 0

	for line in lines:
		if split_string in line:
			line = line[line.index(split_string)+len(split_string):] # Cut out the stuff.
			#print(line)
			if "\")" in line:
				line = line[:line.index("\")")]
				#print(line)
				stuff = bytearray.fromhex(line)
				fh = open("out/"+str(thing), "wb")
				fh.write(stuff)
				fh.close()
				thing += 1
	exit(0)




