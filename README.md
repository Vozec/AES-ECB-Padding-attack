# AES-ECB-Padding-attack
This tool automates and facilitates a padding attack on AES with ECB mode

# Usage :
```python
ecb = Padding_Attack(
	cipher = cipher,
	know = b"ThIs",
	left_pad = True,
	charset = "abcdefghijklmnopqrstuvwxyz"+\
		"ABCDEFGHIJKLMNOPQRSTUVWXYZ" +\
		"0123456789" +\
		"!*-/+_"
)

for flag in ecb.attack():
	print(flag)
```

# Use cases:

- ``plaintext``: *random_padding[1-16] + input + flag*  
- ``plaintext``: *input + flag*

# Input: 

*cipher* is a function that takes bytes as input and returns the encrypted bytes
