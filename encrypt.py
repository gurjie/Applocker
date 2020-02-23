import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def main(): 
    if (len(sys.argv) != 2):
        print("Usage: encrypt.py path \n'path' should include the filename")
        exit
    else:
        # sys.argv[1] is (or should be) the file path
        if(os.access(sys.argv[1],os.F_OK)):
            print("file accessible")
            execute_encryption_routine(sys.argv[1])
        else:
            print("The filepath provided isn't valid")

# Takes as input a binary stream, e.g. target = open(path, "rb")
# Encrypts this data using a default key - this app is not malicious so does not need to be obfuscated or hidden away
# The encrypted file WILL REPLACE the original file's contents with ciphertext, until decrypted. verify this by opening the file with notepad
def execute_encryption_routine(path):

    target = open(path, "rb") # opening for [r]eading as [b]inary
    data = target.read()
    output_file = path # Output file
    key = b'YOUR KEYYOUR KEY' # The key you generated

    # Create cipher object and encrypt the data
    cipher = AES.new(key, AES.MODE_CBC) # Create a AES cipher object with the key using the mode CBC
    ciphered_data = cipher.encrypt(pad(data, AES.block_size)) # Pad the input data and then encrypt

    file_out = open(output_file, "wb") # Open file to write bytes
    file_out.write(cipher.iv) # Write the iv to the output file (will be required for decryption)
    file_out.write(ciphered_data) # Write the varying length cipher text to the file (this is the encrypted data)
    file_out.close()
    print("encryption routine fin")

if __name__ == "__main__": 
    main()