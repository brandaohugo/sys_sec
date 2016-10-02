import sys, hashlib
from Crypto.PublicKey import RSA

f = open(sys.argv[2])
key = RSA.importKey(f.read())
f.close()

input_file = open(sys.argv[1],'r')
file_hash = hashlib.sha256(input_file.read()).hexdigest()
input_file.close()

enc_file_hash = key.encrypt(file_hash, 65555)

input_file = open(sys.argv[1], 'a')
input_file.write(enc_file_hash[0])
input_file.close()