fruit = open("fruits.txt")
content = fruit.read()
fruit.close()
content = content.splitlines()
for i in content:
    print(len(i))


myfile = open("fruits.txt")
content = myfile.read()
myfile.close()
content = content.splitlines()
for i in content:
     print(len(i))