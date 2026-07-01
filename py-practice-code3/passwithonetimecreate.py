
name = {}
x = input("enter user name : ")
y = input("enter pass : ")
name[x] = y

with open("name.txt","a") as file: 
    for n in name: 
        file.write(str(name) + "\n")

print(name)


