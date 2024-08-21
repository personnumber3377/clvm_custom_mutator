

'''

random_shit = random.randrange(MAX_SMALL_INT)
			random_length = min_num_bytes(random_shit)
			bytes_val = integer_val.to_bytes(random_length, 'big')
			assert isinstance(bytes_val, bytes)
			return bytes_val

'''

import random
import math

def min_num_bytes(integer):
	return math.ceil(math.log(integer+1,2) / 8)

MAX_SMALL_INT = 200

if __name__=="__main__":
	random_shit = random.randrange(MAX_SMALL_INT)
	random_length = min_num_bytes(random_shit)
	bytes_val = random_shit.to_bytes(random_length, 'big')
	assert isinstance(bytes_val, bytes)
	# return bytes_val

	print(bytes_val)

	exit(0)

