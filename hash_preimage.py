import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    while(1):
        x = os.urandom(20)
        hex_x = hashlib.sha256(x).hexdigest()
        bin_x = bin(int('1' + hex_x, 16))[3:]
        strlen=len(target_string)
        count=0
        for i in range(strlen):

            if bin_x[255-i]==target_string[strlen-1-i]:
                count+=1

        if count==strlen:
            return (x)
