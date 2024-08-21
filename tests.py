
from main import *


def test_random_node():

	program_data = "ff02ffff0101ffff04ffff0101ffff010180ffff0182133780" #  `(50 60)`
	#print("original data: "+str(program_data))
	new_prog = Program.fromhex(program_data)

	node, parent = select_random_node(new_prog)

	print("node == "+str(node))
	print("parent == "+str(parent))

	print("node.pair == "+str(node.pair))
	print("node.atom == "+str(node.atom))
	return


if __name__=="__main__":

	# First run the test for choosing a random node.

	test_random_node()

	exit(0)
