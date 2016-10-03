import hashlib, sys, os
from hashlib import sha256

def segment_file(input_file, number_of_blocks):
	
	file_length = os.stat(input_file).st_size		

	if (number_of_blocks > file_length):
		return []

	block_size = file_length / number_of_blocks
		
	if (file_length % number_of_blocks) != 0:
		block_size += 1

	result = []
	with open(input_file) as f:
		while True:
			block = f.read(block_size)			
			if len(block) == 0:
				break
			result.append(block)
	return result


def hash_blocks(blocks):
	result = []
	for b in blocks:
		result.append(sha256(b).hexdigest())
	return result


if (len(sys.argv) != 4):
	print("Usage: pyhton blockhash.py <filename1> <filename2> <number_of_blocks>")
	exit(1);

l1 = segment_file(sys.argv[1], (int) (sys.argv[3]))
l2 = segment_file(sys.argv[2], (int) (sys.argv[3]))

h1 = hash_blocks(l1)
h2 = hash_blocks(l2)

matches = 0
for i in range(0,(int) (sys.argv[3])):
	if (h1[i] == h2[i]):
		print("Blocks in position %d match.\n" % i)
		matches += 1
	else:
		print("Blocks in postiion %d do not match.\n" % i)

print("%.2f%% compatibility." % 100 * (matches / (int)(sys.argv[3])))