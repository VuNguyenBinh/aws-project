import os

def delete_file(name):
    os.system("rm " + name)  # command injection

delete_file("test.txt")
