f = open("poem.text")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is persent in the content")

else:
    print("The word twinkle is not persent in the content")

f.close()
