# Applocker
* Needs comments and refactoring *
This is just a personal proejct. 

Python GUI which invokes scheduled tasks to block/unblock files at certain times.

It does so by encrypting the files in place. 

![Sample](/Capture.PNG?raw=true "Screenie")


It follows symlinks/shortcuts to encrypt executables or whatever the target is too

1) Specify target file via GUI to block access to

2) Select time to begin block, select time to restore acceess to the file

3) select frequency of block

4) Hit confirm!

5) Some bash will be executed, invoking a powershell script defining a scheduled task, populated from (safe) user input 

6) creates a entries in task scheduler to execute encrypt.py and decrypt.py with the file input via GUI as argument

7) if decryption fails for some reason, which it shouldnt, run decrypt.py *filepath* to decrypt your file

8) can't create a scheduled block more than once for the same file atm, but its a trivial fix

p.s. the git directory is a mess because i haven't changed gitignore or the dir structure at all, so don't judge :) 
