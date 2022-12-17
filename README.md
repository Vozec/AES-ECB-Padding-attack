# AES-ECB-Padding-attack
This tool automates and facilitates a padding attack on AES with ECB mode

# Usage :
```python
attacker = Padding_Attack(
	cipher = cipher,
	know = b"",
	left_pad = True,
	charset = "abcdefghijklmnopqrstuvwxyz"+\
				"ABCDEFGHIJKLMNOPQRSTUVWXYZ" +\
				"0123456789" +\
				"!*-/+_"
)

for flag in attacker.attack():
	print(flag)
```

# Use cases:

- plaintext: *random_padding[1-16] + input + flag*
  - The size of the *flag* must be a multiple of 16
  
- plaintext: *input + flag*
  - The size of the *flag* is not important
