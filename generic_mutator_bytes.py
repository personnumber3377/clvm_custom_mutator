
import random
import string as string_mod # string.printable

MAX_REPEAT_COUNT = 5

def remove_substring(string: str) -> str:
	if not string:
		return string
	start_index = random.randrange(max(len(string)-1, 1))
	end_index = random.randrange(start_index, len(string))
	return string[:start_index] + string[end_index:]

def multiply_substring(string: str) -> str:
	if not string:
		return string
	start_index = random.randrange(max(len(string)-1, 1))
	end_index = random.randrange(start_index, len(string))
	substr = string[start_index:end_index]
	where_to_place = random.randrange(max(len(string)-1, 1))
	return string[:where_to_place] + (substr * random.randrange(MAX_REPEAT_COUNT)) + string[where_to_place:]

def add_character(string: bytes) -> str:
	#if len(string)-1 >= 1:
	if not string:
		#print("oof")
		return bytes([random.randrange(0,256)])
	where_to_place = random.randrange(max(len(string)-1, 1))
	#print("oof")
	return string[:where_to_place] + bytes([random.randrange(0,256)]) + string[where_to_place:]


MAX_SMALL_INT = 100

def min_num_bytes(integer):
	return math.ceil(math.log(integer+1,2) / 8)

def mutate_generic(string: bytes) -> str: # Mutate a string.


	# First convert to integer and see if it is less than say 256

	stuff = int.from_bytes(string, "big")

	if stuff <= 500:
		if random.randrange(2) == 1: # Select a random integer from a range.
			random_shit = random.randrange(MAX_SMALL_INT)
			random_length = min_num_bytes(random_shit)
			bytes_val = random_shit.to_bytes(random_length, 'big')
			#assert isinstance(bytes_val, bytes)
			return bytes_val

	strat = random.randrange(3)

	match strat:
		case 0:
			# Remove substring
			return remove_substring(string)
		case 1:
			# Multiply substring.
			return multiply_substring(string)
		case 2:
			# Add a character somewhere
			return add_character(string)
		case _:
			print("Invalid")
			assert False
	print("Invalid")
	assert False


