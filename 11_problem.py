
with open("old.text") as f:
    content = f.read()

with open("renamed_by_python.text", "w") as f:
    f.write(content)