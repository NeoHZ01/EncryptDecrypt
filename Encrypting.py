from cryptography.fernet import Fernet

file = open('key.key', 'rb') # Get the key from the file in the read byte form
key = file.read() # The key will be type bytes
file.close()

with open('test.txt', 'rb') as f: # Open the file in read bytes for encryption purposes
    file = f.read()

F = Fernet(key) # Create an object of Fernet and pass the key
encrypted = F.encrypt(file) # Encrypt the file from above

with open('test.txt.encrpyted', 'wb') as f:
    f.write(encrypted)
 
