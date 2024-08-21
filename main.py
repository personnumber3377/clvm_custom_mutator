

import io
import unittest

import sys
from parser import * # For encoding and decoding...
from clvm_rs.program import Program


def custom_mutator(data, max_size, seed, native_mutator): # This is for ruzzyfork
	# The strategy is to first decode the program to a treelike structure and then mutate this tree and then serialize the program back into bytes...
	#prog_tree = decode_tree(data) # Decode to treelike structure
	#prog_tree = mutate_tree(prog_tree) # Mutate
	#mutated_data = encode_tree(prog_tree) # Encode back to bytes
	
	'''


prog = Program() # Initialize the program object...

# fromhex




if len(sys.argv) != 2:
	print("Usage: python3 "+str(sys.argv[0])+" INPUTDATA")
	exit(1)

fh = open(sys.argv[1], "rb")
data = fh.read()
fh.close()


hexadecimal = data.hex()



print("hexadecimal == "+str(hexadecimal))

# hexadecimal = hexadecimal + "fff"

oof = prog.fromhex(hexadecimal)













class SerializeTest(unittest.TestCase):
    def check_serde(self, s):
        v = Program.to(s)
        b = bytes(v)
        f = io.BytesIO()
        v.stream(f)
        b1 = f.getvalue()
        self.assertEqual(b, b1)
        v1 = Program.parse(io.BytesIO(b))
        if v != v1:
            print("%s: %d %s %s" % (v, len(b), b, v1))
            breakpoint()
            b = bytes(v)
            v1 = Program.parse(io.BytesIO(b))
        self.assertEqual(v, v1)





	'''

	


	# program_obj.fromhex("ff32ff3c80") #  `(50 60)`

	#stuff = bytes.fromhex(program_data)


	#shit = Program.parse(io.BytesIO(stuff))


	#program_obj = Program()


	program_data = "ff32ff3c80" #  `(50 60)`

	new_prog = Program.fromhex(program_data)
	print("new_prog._pair == "+str(new_prog._pair))
	
	print("new_prog._pair == "+str(new_prog.pair))
	print("new_prog.atom == "+str(new_prog.atom))

	print(new_prog.pair[1].pair)
	print(new_prog.pair[0].pair)
	print("ooffff")
	print(new_prog.pair[0].atom)
	new_prog.pair[0].atom = b"aaaaaaaaaaaaaaaaa" # Modify the value to some value.
	print(new_prog.pair[0].atom)
	# Now print the bytes which be can get by calling "bytes" on the object.
	print(new_prog.pair[0].pair)

	new_prog._cached_serialization = None

	print("type(new_prog) == "+str(type(new_prog)))

	stuff = bytes(new_prog)

	print(stuff.hex())

	assert stuff != program_data # The program should have changed.

	print("Done!")

	'''


	I think you're printing program_obj instead of new_prog mistakenly
	program_obj.from_hex(..) returns a brand new instance of a program.  You're accessing a @classmethod from the instance is maybe the confusion.  That line should probably be:
	new_prog = Program.fromhex("ff32ff3c80") #  `(50 60)`

	and then print new_prog in all of your stuff below.

	'''



	#print("shit._pair == "+str(shit._pair))

	return



if __name__=="__main__":
	# This main function is just for testing. The fuzzer itself only calls "custom_mutator" with the data.


	if len(sys.argv) != 2:
		print("Usage: python3 "+str(sys.argv[0])+" INPUTDATA")
		exit(1)

	fh = open(sys.argv[1], "rb")
	data = fh.read()
	fh.close()

	databytes = bytearray(data) # Convert to bytearray as the fuzzer would pass the data to the "custom_mutator" as a bytearray...

	new_data = custom_mutator(databytes, 10000000, 100, None)

	print("Here is the mutated data: ")

	print(new_data)



	exit(0)

