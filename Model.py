import os
import tempfile
import time
import logging
class Model:

    def __init__(self): 
        print("Model instantiated")

    def fileAccessible(self, file):
        if (os.access(file,os.F_OK) == True):
            return 1
        else:
            return 0

    def createTmpPowershell(self):
        script = tempfile.NamedTemporaryFile(suffix=".ps1", mode="w+")
        logging.warning("Created temp file to hold script: "+script.name)
        return script

    def execute_daily(self, sh, sm, eh, em, file):
        if (self.fileAccessible(file) == 1):
            script = self.createTmpPowershell()
            if (self.fileAccessible(script.name)):
               return 1 
            else:
                return 2
        else:
            return 0

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
