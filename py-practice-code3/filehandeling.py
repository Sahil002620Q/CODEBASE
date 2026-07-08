item = "empty file"
file = open("filesm.txt","w")
file.write(item)
file.close()
print(file)

file = open("filesm.txt","r")
c = file.read()
file.close()
print(c)



cont = str({"key":"value"})
with open("javsrcobjnot.json","w") as file:
    file.write(cont)
