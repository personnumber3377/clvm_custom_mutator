

import io
import unittest
import random

from generic_mutator_bytes import * # For the generic mutator...
import sys
from parser import * # For encoding and decoding...
from clvm_rs.program import Program


def ashex(string: str):
	return "".join("{:02x}".format(ord(c)) for c in string)


'''

def get_all_paths_recursive(cur_node, current_path):
	out = [current_path]
	for i, child in enumerate(cur_node): # Loop over all child nodes...
		# print("current_path + [i] == "+str(current_path + [i]))
		# out.append(get_all_paths_recursive(child, current_path + [i]))
		out += get_all_paths_recursive(child, current_path + [i])
	return out


def get_all_paths(tree):
	return get_all_paths_recursive(tree, [])






def test_uncurry_top_level_garbage():
    # there's garbage at the end of the top-level list
    # `(a (q . 1) (c (q . 1) (q . 1)) (q . 0x1337))`
    plus = Program.fromhex("ff02ffff0101ffff04ffff0101ffff010180ffff0182133780")
    assert plus.uncurry() == (plus, None)



'''


def get_all_paths_recursive(cur_node, current_path):
	out = [current_path]
	if cur_node.pair:

		for i, child in enumerate(cur_node.pair): # Loop over all child nodes... (new_prog.pair)
			# print("current_path + [i] == "+str(current_path + [i]))
			# out.append(get_all_paths_recursive(child, current_path + [i]))
			out += get_all_paths_recursive(child, current_path + [i])
	else:
		#print("Encountered atom: "+str(cur_node.atom))
		#print("cur_node == "+str(cur_node))
		#print("cur_node.atom == "+str(cur_node.atom))
		#print("cur_node.pair == "+str(cur_node.pair))
		#assert cur_node.atom
		if not cur_node.atom: # 0x80 or "nil" https://chialisp.com/clvm/#nil
			# NOTE: This acts normally (for now) when the node is "nil" , but if this causes problems, change this behaviour to do something else in this "if not" case.
			return out
		return out
	return out

def get_all_paths(program):
	#print("program.pair == "+str(program.pair[1].pair))
	return get_all_paths_recursive(program, [])


def select_random_node(program): # Select a random node from the program...
	# Thanks to https://www.geeksforgeeks.org/select-random-node-tree-equal-probability/
	all_paths = get_all_paths(program)
	rand_path = random.choice(all_paths)
	parent = None
	out = program
	for ind in rand_path:
		parent = out
		out = out.pair[ind]
	return out, parent


def isatom(node): # Returns true, if node is an atom, otherwise returns false
	if not node.pair: # No pair... therefore atom
		return True
	return False # pair exists, therefore not atom

def mutate_atom(node): # Mutates an atom in-place.
	assert isatom(node) # Node should be atom.
	node.atom = mutate_generic(node.atom) # Call the generic mutator on the atom.
	return

def mutate_program(program): # Mutate the program object...

	# First get a random node to mutate, then select mutation strategy, mutate the program in-place.

	rand_node = select_random_node(program)

	if isatom(rand_node):
		# Mutate atom.
		mutate_atom(rand_node)

	return


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


	assert isinstance(data, bytearray)

	program_data = "ff32ff3c80" #  `(50 60)`
	print("original data: "+str(program_data))
	new_prog = Program.fromhex(program_data)
	print("new_prog._pair == "+str(new_prog._pair))
	
	print("new_prog._pair == "+str(new_prog.pair))
	print("new_prog.atom == "+str(new_prog.atom))







	print(new_prog.pair[1].pair)
	print(new_prog.pair[0].pair)
	print("ooffff")
	print(new_prog.pair[0].atom)


	# Mutate program...

	#mutate_program(new_prog)
	print("paskaaaaaaa")
	print(list(new_prog.pair))


	new_prog.pair[0].atom = b"aaaaaaaaaaaaaaaaa" # Modify the value to some value.
	print(new_prog.pair[0].atom)
	# Now print the bytes which be can get by calling "bytes" on the object.
	print(new_prog.pair[0].pair)

	new_prog._cached_serialization = None

	print("type(new_prog) == "+str(type(new_prog)))

	stuff = bytes(new_prog)


	print("="*20)
	print(ashex(str(stuff.hex())))

	print(ashex(str(program_data)))
	print("="*20)
	print("stuff: "+str(stuff.hex()))

	print("program_data == "+str(program_data))
	print("str(stuff) == str(program_data) == "+str(str(stuff) == str(program_data)))
	if str(stuff.hex()) == str(program_data): # Check if the program got actually modified.
		print("It is still the same!")
		exit(1)

	
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

