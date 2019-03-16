# @mustafasakalli
import os, sys
from pathlib import Path 

home = str(Path.home())
print (home) #user's home directory has been printed.

jailpath = home + "/jail"

os.mkdir (jailpath);
print (jailpath)  #user's new jail directory has been set

os.chroot(jailpath)
print ("changed root path!!!") # You can see some "sudo" errors on this step
