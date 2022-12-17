from binascii import hexlify,unhexlify
from os import urandom
from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from AES_ECB_Padding_Attack import *

engine = AES.new(urandom(16), AES.MODE_ECB)

##########################################################
# Case 1 : random_padding[1-16] + input + flag(len%16=0) #
##########################################################

def cipher_1(data:bytes) -> bytes:
	secret = b'ThIs_Is_tH3_Sec4Et!!!!0123456789'
	rdn_padding = b'X'*5
	return engine.encrypt(
		pad(rdn_padding+data+secret,16)
	)

ecb_1 = Padding_Attack(
	cipher = cipher_1,
	know = b"ThIs",
	left_pad = True
)

for flag in ecb_1.attack():
	print(flag)

####################################
# Case 2 : plaintext: input + flag #
####################################
def cipher_2(data:bytes) -> bytes:
	secret = b'ThIs_Is_tH3_Sec4Et!'
	return engine.encrypt(
		pad(data+secret,16)
	)
ecb_2 = Padding_Attack(
	cipher = cipher_2,
	know = b"ThIs",
	left_pad = False
)


for flag in ecb_2.attack():
	print(flag)