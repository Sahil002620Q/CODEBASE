import json
import lib
name = {}
x = input("enter user name : ")
y = input("enter pass : ")
name[x] = y



with open("name.json","w") as file: # "a" will make new dict ie {}  + {} not { k:v +k:v}
    for n in name: 
        json.dump(name,file,)
        # file.write(str(name) + "\n")


lib.lineanime(name)


