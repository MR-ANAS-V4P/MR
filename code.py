import os, sys
os.system("git pull")
try:
    __import__("ANAS-M1").anas()
except Exception as e:
    exit(str(e))