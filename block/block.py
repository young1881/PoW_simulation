import random
import sys
import time
from hashlib import sha256


class Block:

    def __init__(self, previous_hash, bits="0000"):
        self.previous_hash = previous_hash
        self.nonce = str(random.randint(0, sys.maxsize))
        self.time_stamp = time.time()
        self.bits = bits

    # return the hash value of block
    def hash(self):
        s = sha256()
        s.update(self.previous_hash.encode("utf-8"))
        s.update(self.nonce.encode("utf-8"))
        s.update(str(self.time_stamp).encode("utf-8"))
        hash_value = s.hexdigest()
        return hash_value

    #  if the current hash value is less than t, return True else return False
    def check_nonce(self):
        hash_value = hash(self)
        return hash_value.startswith(self.bits)

    # set this block to be genesis
    def set_genesis(self):
        self.nonce = str(0)
        self.time_stamp = 0
        self.previous_hash = str(0)

