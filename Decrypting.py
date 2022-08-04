from cryptography.fernet import Fernet

file = open('key.key', 'rb') # Get the key from the file in the read byte form
key = file.read() # The key will be type bytes

with open('test.txt.encrpyted', 'rb') as f: # Open the encrypted file in read bytes for decryption purposes
    file = f.read()

F = Fernet(key) # Create an object of Fernet and pass the key
encrypted = F.decrypt(file) # Decrypt the file from above

with open('test.txt.decrpyted', 'wb') as f:
    f.write(encrypted)
