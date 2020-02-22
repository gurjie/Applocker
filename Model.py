import os
import tempfile
import time
import logging
import socket
import secrets
import hashlib
from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad



class Error(Exception):
    """Base for exception classes"""
    pass

class FilePathError(Error):
    """Raised when a file can't be reached"""
    def __init__(self, file):
        self.file = file

    def getFile(self):
        return self.file
    pass

class TmpFileCreateError(Error):
    """Raised tmp powershell script can't be written"""
    def __init__(self, file):
        self.file = file

    def getFile(self):
        return self.file
    pass

class TimeError(Error):
    """Raised tmp powershell script can't be written"""
    pass

class DirectoryCreation(Error):
    """Raised tmp powershell script can't be written"""
    pass

class Model:

    def __init__(self): 
        self.dirName = os.getenv('LOCALAPPDATA')+"\Applocker"
        print("dirname is "+self.dirName)
        self.createAppDirectory()
        print("Model instantiated")

    def fileAccessible(self, file):
        return os.access(file,os.F_OK)


    def createTmpPowershell(self):
        script = tempfile.NamedTemporaryFile(suffix=".ps1", mode="w+")
        logging.warning("Created temp file to hold script: "+script.name)
        return script

    def formatTime(self, hh, mm):
        if(int(hh)<10):
            hh = "0"+hh
        if(int(mm)<10):
            mm = "0"+mm
        return hh+":"+mm

    def validateTime(self,sh,sm,eh,em):
        if ( (sh.isdigit()) & (sm.isdigit()) & (eh.isdigit()) & (em.isdigit()) ):
            if ( (0 <= int(sh)<24) & (0 <= int(sm)<60) & (0 <= int(eh)<24) & (0 <= int(em)<60) ):
                return True
            else:
                return False
        else:
            return False

    def buildTaskDaily(self, formatted_time,path):
        tt = '$Time = New-ScheduledTaskTrigger -At ' + formatted_time + ' -Daily\n'
        user = socket.gethostname().lower() + "\\" + os.getlogin()+"\n"
        program = '$PS = New-ScheduledTaskAction -Execute \"'+path+'\"\n'
        # extract filename from path, to set as task name
        index = path.rfind("/")
        filename = path[index:].replace("/","")
        register = 'Register-ScheduledTask -TaskName "block "'+filename+' -Trigger $Time -User $User -Action $PS'
        print(tt+user+program+register)
        key_file_name = self.generateKeyfileName(filename)
        target = open(path, "rb") # opening for [r]eading as [b]inary
        data = target.read()
        extension = os.path.splitext(path)[1]
        #self.encrypt(data)
        self.decrypt(data,filename)
        #self.generateKeys()
        #f = open(key_file_name,"w")
        #f.close()

    # generate a name for the file the encryption key will be stored as for the routine
    def generateKeyfileName(self,filename): 
        salt = secrets.token_urlsafe(5)
        salted_filename = filename+salt
        #print(salted_filename)
        hashed = hashlib.sha256(salted_filename.encode('utf-8'))
        return hashed.hexdigest()

    def encrypt(self,target):
        #secret_code = "Unguessable"
        #key = RSA.generate(2048)
        #encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,protection="scryptAndAES256-CBC")
        #file_out = open(self.dirName+"\\"+"rsa_key.bin", "wb")
        #file_out.write(encrypted_key)
        output_file = self.dirName+'\encrypted.bin' # Output file
        data = target # Must be a bytes object
        key = b'YOUR KEYYOUR KEY' # The key you generated

        # Create cipher object and encrypt the data
        cipher = AES.new(key, AES.MODE_CBC) # Create a AES cipher object with the key using the mode CBC
        ciphered_data = cipher.encrypt(pad(data, AES.block_size)) # Pad the input data and then encrypt

        file_out = open(output_file, "wb") # Open file to write bytes
        file_out.write(cipher.iv) # Write the iv to the output file (will be required for decryption)
        file_out.write(ciphered_data) # Write the varying length cipher text to the file (this is the encrypted data)
        file_out.close()
        print("encryption routine fin")

    def decrypt(self,target,filename):
        input_file = self.dirName+'\encrypted.bin' # Input file
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
        os.rename(input_file,self.dirName+"\\"+filename)
    # creates directory for the app if it doesn't exist, to host local files etc
    def createAppDirectory(self):
        if (self.fileAccessible(self.dirName)):
            print("Wow it exists!")
        else:
            print("it doesn't exist")
        if not os.path.exists(self.dirName):
            os.mkdir(self.dirName)
            print("Directory " , self.dirName ,  " Created ")
            if not os.path.isdir(self.dirName):
                print("WTF IT DIDNT CREATE")
                raise
            else:
                print("craeted")

        else:    
            print("Directory " , self.dirName ,  " already exists")


    def execute_daily(self, sh, sm, eh, em, file):
        if (self.fileAccessible(file)):
            script = self.createTmpPowershell()
            if (self.fileAccessible(script.name)):
                if (self.validateTime(sh,sm,eh,em)):
                    start = self.formatTime(sh,sm)
                    end = self.formatTime(eh,em)
                    self.buildTaskDaily(start,file)
                else:
                    raise TimeError
            else:
                raise TmpFileCreateError(file)
        else:
            raise FilePathError(file)

        """
        try:
            # build the contents of the scheduled task
            tt = '$Time = New-ScheduledTaskTrigger -At 13:37 -Once\n'
            user = '$User = \"desktop-q3h5lqm\\44792\"\n'
            program = '$PS = New-ScheduledTaskAction -Execute \"'+self.path+'\"\n'
            register = 'Register-ScheduledTask -TaskName "my ball" -Trigger $Time -User $User -Action $PS'
            script.write(tt+user+program)
            script.seek(0)
            print(script.read())
            
        finally:
            print("Closing the temp file")
            script.close() #5
        """

    def execute_specified(self, sh, sm, eh, em, file):

        """
        script = tempfile.NamedTemporaryFile(suffix=".ps1", mode="w+")
        logging.warning("Created temp file to hold script: "+script.name)
        try:
            # build the contents of the scheduled task
            tt = '$Time = New-ScheduledTaskTrigger -At 13:37 -Once\n'
            user = '$User = \"desktop-q3h5lqm\\44792\"\n'
            program = '$PS = New-ScheduledTaskAction -Execute \"'+self.path+'\"\n'
            register = 'Register-ScheduledTask -TaskName "my ball" -Trigger $Time -User $User -Action $PS'
            script.write(tt+user+program)
            script.seek(0)
            print(script.read())
            
        finally:
            print("Closing the temp file")
            script.close() #5
        """
