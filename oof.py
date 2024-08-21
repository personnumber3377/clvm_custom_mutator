
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

	'''

	program_obj = Program()

	new_prog = program_obj.fromhex("ff32ff3c80") # Convert to hex before passing to the function...

	# See the _pair object.

	#print("new_prog._pair == "+str(new_prog._pair))

	print("_pair == "+str(new_prog._pair))
	print("program_obj == "+str(program_obj._pair))
	print("program_obj == "+str(program_obj.atom))
	print("program_obj == "+str(new_prog.atom))
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

