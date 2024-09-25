with open("this.text") as f:
    content = f.read()

with open("this_copy.text", "w") as f:
    f.write(content)