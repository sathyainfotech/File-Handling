import os
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
  print("File Deleted Successfully")
else:
  print("The file does not exist")