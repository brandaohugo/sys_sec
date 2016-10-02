import sys, hashlib
from Crypto.PublicKey import RSA

f = open(sys.argv[2])
key = RSA.importKey(f.read())
f.close()

input_file = open(sys.argv[1],'r')
input_data = input_file.read()
input_file.close()

original_data = input_data[:-256]
cypher = input_data[-256:]
plain_hash = key.decrypt(cypher)
file_hash = hashlib.sha256(original_data).hexdigest()


if (plain_hash == file_hash):
	print("Signature confirmed")
else: 
	print("Failed to confirm signature")