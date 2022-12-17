from binascii import unhexlify,hexlify
import string


class Padding_Attack:
	def __init__(self,cipher,know=b"",left_pad=False,charset=string.printable[:-5]):
		self.cipher = cipher
		self.k = know
		self.left_pad = 16
		self.left_block = left_pad
		self.charset = charset

	def left_block_len(self):
		last = len(self.cipher(b''))//16
		for i in range(1,16):
			r = len(self.cipher(b'A'*i))//16
			if r > last:
				return i
		return 16

	def verif_pad(self):
		return len(self.cipher(b'A'*self.left_pad))+16 == \
			len(self.cipher(b'A'*(self.left_pad+16)))

	def splited(self,data:bytes) -> list:
		data = hexlify(data)
		return [data[32*i:32*(i+1)].decode() for i in range(len(data)//32)]
		
	def get_vuln_bloc(self):
		ref = self.splited(self.cipher(b'A'*self.left_pad+b'B'*16))
		dif = self.splited(self.cipher(b'A'*self.left_pad+b'C'*16))
		for i in range(len(ref)):
			if ref[i] != dif[i]:
				return i

	def attack(self):
		if self.left_block:
			self.left_pad = self.left_block_len()

		assert self.verif_pad(), "There is a padding problem !" 
		block = self.get_vuln_bloc()

		idx_blc = 1
		while True:
			ref = self.splited(
				self.cipher(b'B'*self.left_pad + b'A'*(16*idx_blc-1-len(self.k)))
			)[idx_blc]

			before = self.k
			for l in self.charset:
				payload = b'B'*self.left_pad + b'A'* (16*idx_blc-1 - len(self.k)) + self.k + bytes(l,'utf-8')
				r = self.splited(self.cipher(payload))[idx_blc]
				if r == ref:
					self.k += bytes(l,'utf-8')
					idx_blc = (len(self.k) // 16) + block
					yield self.k
					break
					
			if before == self.k:
				break
		return self.k