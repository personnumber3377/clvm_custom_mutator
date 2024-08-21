
from clvm_rs.program import Program

def minimal_example():
	program_data = "ff32ff3c80" #  `(50 60)`
	new_prog = Program.fromhex(program_data)
	print("Value before modification: "+str(new_prog.pair[0].atom))
	new_prog.pair[0].atom = b"examplevalue" # Modify the value to some value.
	print("Value after modification: "+str(new_prog.pair[0].atom))
	new_prog._cached_serialization = None # Set cache to none, such that clvm_rs actually serializes the program again.
	stuff = bytes(new_prog)
	if str(stuff.hex()) == str(program_data): # Check if the program got actually modified.
		print("It is still the same!")
		print("Fail!")
		return 1
	print("stuff.hex() == "+str(stuff.hex()))
	print("Success! Program got modified!")
	return 0

if __name__=="__main__":
	# This main function showcases the bug.
	ret = minimal_example()
	exit(ret)

