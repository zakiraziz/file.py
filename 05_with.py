f = open("file.text")
print(f.read())
f.close()
 
# the same can be writen useing with statment like this:
with open("file.text") as f:
    print(f.read())

# you don have to explicity close  the file
