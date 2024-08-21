
# This file defines the parser which converts the binary data to a treelike structure.

from tree import *


CONS_PAIR = 0xFF # Cons pair identifier.


def decode_tree(data: bytes): # Main decoding function.
	# Parse data
	data_pointer = 0

	if len(data) == 0:
		return


	output_tree = ProgramTree() # Output tree.

	while True: # Loop over data:
		# ooofff

		cur_byte = data[data_pointer]

		# 0xFF

		if cur_byte:
			return



	return output_tree

