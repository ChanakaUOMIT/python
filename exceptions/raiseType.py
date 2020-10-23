# try to raise TypeError

a = "This language is Fun!"

if not type(a) is int:
    raise Exception("Only integer numbers are allowed here!")
