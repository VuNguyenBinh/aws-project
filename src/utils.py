def unused_function(a, b, c):
    d = 10  # unused var
    return a

password = "hardcoded"  # another  hotspot

def insecure():
    import subprocess
    subprocess.call("ls -la", shell=True)  # unsafe
