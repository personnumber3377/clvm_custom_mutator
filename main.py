

import io
import unittest
import random

from generic_mutator_bytes import * # For the generic mutator...
import sys
from parser import * # For encoding and decoding...
from clvm_rs.program import Program
import copy


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

def add_node(where_to_add, rand_node): # "where_to_add" is the node where we add a copy of the node "rand_node"...

	if not isatom(where_to_add): # Where we add the thing is not an atom (aka a "cons pair"), so I think we can just put it there straight away...
		print("poopoo")
		where_to_add = rand_node #copy.deepcopy(rand_node)
	else: # The node where we add is an atom...
		return	


	return

def mutate_program(program): # Mutate the program object...

	# First get a random node to mutate, then select mutation strategy, mutate the program in-place.

	rand_node, _ = select_random_node(program) # Parent is left unused
	print("rand_node == "+str(rand_node))
	print("rand_node.atom == "+str(rand_node.atom))
	print("rand_node.pair == "+str(rand_node.pair))
	if isatom(rand_node):
		# Mutate atom.
		mutate_atom(rand_node)
	else:
		# Mutate a so called "cons pair" (https://chialisp.com/clvm/#cons-pairs)

		cons_pair_thing = random.randrange(2) # select strategy...

		if cons_pair_thing == 0: # Remove node entirely and replace with atom.
			
			where_to_add = rand_node
			count = 10 # How many tries
			while where_to_add == rand_node: # Do not select the same node.
				where_to_add, _ = select_random_node(program) # Get another
				count -= 1 # Subtract from count
				if count == 0:
					# If we didn't pick another node within ten tries, then just return the original
					return

			# Add the selected node to the place which we 
			assert where_to_add != rand_node
			#add_node(where_to_add, rand_node) # Add the node.
			print("FuckFuck!!!!")
			print("where_to_add == "+str(where_to_add))
			print("rand_node == "+str(rand_node))

			where_to_add = rand_node
			print("After...")
			print("where_to_add == "+str(where_to_add))
			print("rand_node == "+str(rand_node))
			assert where_to_add == rand_node

			return
		elif cons_pair_thing == 1: # Copy node and add it somewhere else
			return
		else:
			print("Invalid")
			exit(1)
		return


	return


def custom_mutator(data, max_size, seed, native_mutator): # This is for ruzzyfork
	# The strategy is to first decode the program to a treelike structure and then mutate this tree and then serialize the program back into bytes...
	assert isinstance(data, bytearray) # Sanity checking...

	program_data = data.hex() # Convert to hex representation
	new_prog = Program.fromhex(program_data)

	# Mutate program...
	mutate_program(new_prog)

	new_prog._cached_serialization = None # This is to get the new serialization, not the cached one.

	#print("type(new_prog) == "+str(type(new_prog)))

	stuff = bytes(new_prog)
	output = bytearray(stuff)

	# Hard cap...

	if len(output) >= max_size:
		output = output[:max_size]

	return output # Return the mutated program as bytearray...



if __name__=="__main__":
	# This main function is just for testing. The fuzzer itself only calls "custom_mutator" with the data.


	# program_data = "ff32ff3c80"

	program_data = "ff02ffff0101ffff04ffff0101ffff010180ffff0182133780"

	byte_stuff = bytes.fromhex(program_data)

	databytes = bytearray(byte_stuff) # Convert to bytearray as the fuzzer would pass the data to the "custom_mutator" as a bytearray...

	new_data = custom_mutator(databytes, 10000000, 100, None)

	assert isinstance(new_data, bytearray)


	print("Here is the mutated data: ")

	print(new_data)

	fh = open("output.bin", "wb")

	fh.write(bytes(new_data))

	fh.close()

	print("Saved output to \"output.bin\"! Try disassembling the file to see the mutated program! (with \"cdv clsp disassemble\")")

	exit(0)

