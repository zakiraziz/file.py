word = ["Donkey", "bad", "ganda"]

try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found, creating a new one...")
    with open("file.txt", "w") as f:
        f.write("This is a test file. Donkey is a word in this file.")
    with open("file.txt", "r") as f:
        content = f.read()
for word in word:
    content = content.replace(word, "#" * len(word))


with open("file.txt", "w") as f:
    f.write(content)
