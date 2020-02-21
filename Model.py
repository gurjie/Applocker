import os
import tempfile
import time
import logging

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

class Model:

    def __init__(self): 
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



    def execute_daily(self, sh, sm, eh, em, file):
        if (self.fileAccessible(file)):
            script = self.createTmpPowershell()
            if (self.fileAccessible(script.name)):
                if (self.validateTime(sh,sm,eh,em)):
                    print("made it!")
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
