# Random password Generator
import random 
import string

pass_len = 12
chaValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(chaValues)

print("your random password is :", password)