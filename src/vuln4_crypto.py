import hashlib

SECRET_KEY = "123456"  # hardcoded

def weak_md5(data):
    return hashlib.md5(data.encode()).hexdigest()  # weak  algorithm

print(weak_md5("password"))
