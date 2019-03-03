import os.path, time

print (" a.txt is last modified at: ")
print(time.ctime(os.path.getmtime("a.txt")))
print (" a.txt is created at: " )
print(time.ctime(os.path.getctime("a.txt")))

print ("------------------------------------")

print (" b.txt is last modified at: ")
print(time.ctime(os.path.getmtime("b.txt")))
print (" b.txt is created at: ")
print(time.ctime(os.path.getctime("b.txt")))

print ("------------------------------------")

print (" 0.py is last modified at: ")
print(time.ctime(os.path.getmtime("0.py")))
print (" 0.py is created at: ")
print(time.ctime(os.path.getctime("0.py")))
