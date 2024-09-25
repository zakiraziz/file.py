

with open("log.text") as f:
    line = f.readline()

lineno = 1 
for line in line:
    if("python" in line):
        print("Yes python is present. line no: {line}")
        break
    lineno += 1

else:
    print("No python is no present")