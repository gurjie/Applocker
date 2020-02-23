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
import subprocess
from subprocess import call

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

class decryptionPaddingError(Error):
    """Raised tmp powershell script can't be written"""
    pass

class encryptionError(Error):
    """Raised tmp powershell script can't be written"""
    pass

class decryptionError(Error):
    """Raised tmp powershell script can't be written"""
    pass

class Model:

    def __init__(self): 
        # set the dirname for any app data
        self.dirName = os.getenv('LOCALAPPDATA')+"\Applocker"
        self.createAppDirectory()

    def fileAccessible(self, file):
        return os.access(file,os.F_OK)


    def createTmpPowershell(self):
        script = tempfile.NamedTemporaryFile(suffix=".ps1", mode="w+")
        return script

    def validateTimeformat(self,time):
        if(time=="00" or time=="01" or time=="02" or time=="03" or time=="04" or time=="05" or time=="06" or time=="07" or time=="08" or time=="09"):
            return False
        else:
            return True

    def formatTime(self, hh, mm):
        if(int(hh)<10 & self.validateTimeformat(hh)==True):
            hh = "0"+hh
        if(int(mm)<10 & self.validateTimeformat(hh)==False):
            mm = "0"+mm
        return hh+":"+mm

    # validate start hour, start minute, end hour, end minute from GUI input, that they're suitable for scheduled tasks
    # the file encryption routine will begin at sh:sm and decryption will run at eh:em
    def validateTime(self,sh,sm,eh,em):
        if ( (sh.isdigit()) & (sm.isdigit()) & (eh.isdigit()) & (em.isdigit()) ):
            if ( (0 <= int(sh)<24) & (0 <= int(sm)<60) & (0 <= int(eh)<24) & (0 <= int(em)<60) ):
                return True
            else:
                return False
        else:
            return False

    def buildEncryptionPowershell(self, path):
        currentDir = os.path.dirname(os.path.realpath(__file__))
        path_to_encryption_routine = currentDir+"\encrypt.py"
        path_to_powershell = self.dirName+"\encrypt "+self.getFilenameFromPath(path)+".ps1"
        powershell = open(path_to_powershell, 'w')
        powershell.write("python "+self.sanitizePath(path_to_encryption_routine)+" "+self.sanitizePath(path))
        powershell.close()
        return self.sanitizePath(path_to_powershell)

    def buildDecryptionPowershell(self, path):
        currentDir = os.path.dirname(os.path.realpath(__file__))
        path_to_decryption_routine = currentDir+"\decrypt.py"
        path_to_powershell = self.dirName+"\decrypt "+self.getFilenameFromPath(path)+".ps1"
        powershell = open(path_to_powershell, 'w')
        powershell.write("python "+self.sanitizePath(path_to_decryption_routine)+" "+self.sanitizePath(path))
        powershell.close()
        return self.sanitizePath(path_to_powershell)

    def sanitizePath(self, path):
        exploded = path.split("\\")
        if(len(exploded)==1):
            exploded = path.split("/")
        reconstructed = ""
        i = 0
        for i in range(0,len(exploded)):
            reconstructed = reconstructed + exploded[i]+"'/'"
        index = reconstructed.find("'")
        rindex = reconstructed.rfind("'")
        reconstructed = reconstructed[0:index]+reconstructed[index+1:rindex]+reconstructed[rindex+1:]
        r2index = reconstructed.rfind("/")
        reconstructed = reconstructed[0:r2index]
        return reconstructed

    def getFilenameFromPath(self, path):
        # extract filename from path
        index = path.rfind("/")
        filename = path[index:].replace("/","")
        return filename

    def schedule_lock_app(self, formatted_time,path):
        target = open(path, "rb") # opening for [r]eading as [b]inary
        data = target.read()
        # run a quick 'dummy' encryption + decryption to determine if the scheduled task should proceed to create
        try:
            self.encrypt(data,path,self.getFilenameFromPath(path))
        except:
            raise encryptionError
        try:
            self.decrypt(data,path,self.getFilenameFromPath(path))
        except:
            raise decryptionError

        # Build the powershell variables / executable
        encryption_powershell = self.buildEncryptionPowershell(path) # the ps used to invoke encrypt.py on $path
        print(encryption_powershell)

        
        tt = '$Time = New-ScheduledTaskTrigger -At ' + formatted_time + ' -Daily\n'
        user = '$User = "'+socket.gethostname().lower() + "\\" + os.getlogin()+'"\n'
        program = '$PS = New-ScheduledTaskAction -Execute \"Powershell.exe\" -Argument "'+encryption_powershell+'"\n'
        register = 'Register-ScheduledTask -TaskName "block '+self.getFilenameFromPath(path)+'" -Trigger $Time -User $User -Action $PS '
        #print(tt+user+program+register)
        # Create the temp powershell script to register in scheduled task
        script = open(self.dirName+"\Schedule_encryption.ps1",'w')
        script.write(tt+user+program+register)
        script.close()
        return_code = call("Powershell.exe -executionpolicy remotesigned -File "+script.name, shell=True)  ## return 0 is successful
        print(return_code)
        os.remove(script.name)

        #key_file_name = self.generateKeyfileName(filename)

    def schedule_unlock_app(self, formatted_time,path):

        # Build the powershell variables / executable
        decryption_powershell = self.buildDecryptionPowershell(path) # the ps used to invoke encrypt.py on $path
        print(decryption_powershell)

        
        tt = '$Time = New-ScheduledTaskTrigger -At ' + formatted_time + ' -Daily\n'
        user = '$User = "'+socket.gethostname().lower() + "\\" + os.getlogin()+'"\n'
        program = '$PS = New-ScheduledTaskAction -Execute \"Powershell.exe\" -Argument "'+decryption_powershell+'"\n'
        register = 'Register-ScheduledTask -TaskName "unblock '+self.getFilenameFromPath(path)+'" -Trigger $Time -User $User -Action $PS '
        #print(tt+user+program+register)
        # Create the temp powershell script to register in scheduled task
        script = open(self.dirName+"\Schedule_decryption.ps1",'w')
        script.write(tt+user+program+register)
        script.close()
        return_code = call("Powershell.exe -executionpolicy remotesigned -File "+script.name, shell=True)  ## return 0 is successful
        print(return_code)
        os.remove(script.name)
        

    # generate a name for the file the encryption key will be stored as for the routine
    def generateKeyfileName(self,filename): 
        salt = secrets.token_urlsafe(5)
        salted_filename = filename+salt
        #print(salted_filename)
        hashed = hashlib.sha256(salted_filename.encode('utf-8'))
        return hashed.hexdigest()


    def encrypt(self,target, path, filename):
        output_file = path # Output file
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

    def decrypt(self,target, path, filename):
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
        # creates directory for the app if it doesn't exist, to host local files etc

    # create appdata entry for this app, to store any files or data specific to it 
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
                #raise
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
                    self.schedule_lock_app(start,file)
                    self.schedule_unlock_app(end,file)
                    return "success"
                else:
                    raise TimeError
            else:
                raise TmpFileCreateError(file)
        else:
            raise FilePathError(file)

