with open("log.text") as f:
    content = f.read()

if("python" in content):
    print("Yes oython is present")
else:
    print("No python is not present")