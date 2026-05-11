import os
import shutil

current_dir = os.getcwd()

print("Booting AstroOS")
print("=====================")
print("       ASTROOS")
print("          v1.0")
print("====================")
print("copyright 2026 John Khaleed")
print("BTW ITS NOT FINISHED!!!!!!!!!!!!!!!")
print ("Any feedback is appreciated!")
print()

def new_func():
    print("Just wait......")

while True:
  cmd = input("AstroOS>")

  if cmd == "create":
      name = input("File name: ")
      content = input("Content:")
      open(name, "w").write(content)
      print ("File Created :)")


  elif cmd == "dir":
      print (os.listdir())

  elif cmd.startswith("cd"):
      path = cmd[3:]

      try:
          os.chdir(path)
          current_dir = os.getcwd()
          print ("Moved to:", current_dir)
      except:
          print("Directory not found. create it first")

  elif cmd.startswith("mkdir"):
      folder  = cmd[6:]
      os.makedirs(folder, exist_ok=True)
      print("DIRECTORY HAS BEEN CREATED. YOU CAN NOW OPEN IT :)")

  elif cmd == "open":
      name = input("File Name:")
      try:
          print(open(name, "r").read())
      except:
          print("File Not Found. Create it First.")

  if cmd == "help":
     print("Commands: help, echo, exit, info, dir, mkdir, cd, create, open")

  elif cmd == "info":
      print("VERSION: V1.0. \n\nSTATUS:IN DEVELOPMENT. HANG ON!")

  elif cmd.startswith("echo"):
      print(cmd[5:])

  elif cmd== "exit":
      print ("Shutting down and Saving AstroOS.....")
      break

else:
     new_func()
 