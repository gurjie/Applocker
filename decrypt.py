import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
from win10toast import ToastNotifier


def main(): 
    if (len(sys.argv) != 2):
        print("Usage: decrypt.py path \n'path' should include the filename")
        exit
    else:
        # sys.argv[1] is (or should be) the file path
        if(os.access(sys.argv[1],os.F_OK)):
            print("file accessible")
            try:
                execute_decryption_routine(sys.argv[1])
                toaster = ToastNotifier()
                toaster.show_toast("Applock Decryption Success","Applock successfully ran the Decryption routine on "+sys.argv[1]+". The file's now UNLOCKED.")
            except:
                toaster = ToastNotifier()
                toaster.show_toast("Applock Decryption FAILURE","Applock FAILED to run the Decryption routine on "+sys.argv[1]+". Please review scheduled task")
        else:
            print("The filepath provided isn't valid")

# Takes as input a binary stream, e.g. target = open(path, "rb")
# Encrypts this data using a default key - this app is not malicious so does not need to be obfuscated or hidden away
# The encrypted file WILL REPLACE the original file's contents with ciphertext, until decrypted. verify this by opening the file with notepad
def execute_decryption_routine(path):
    input_file = path # Input file
    key = b'YOUR KEYYOUR KEY' # The key used for encryption (do not store/read this from the file)

    # Read the data from the file
    file_in = open(input_file, 'rb') # Open the file to read bytes
    iv = file_in.read(16) # Read the iv out - this is 16 bytes long
    ciphered_data = file_in.read() # Read the rest of the data
    file_in.close()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
    original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) # Decrypt and then up-pad the result
    file_out = open(input_file, "wb") # Open file to write bytes
    file_out.write(original_data)
    file_out.close()
    print("decryption routine fin")

if __name__ == "__main__": 
    main()