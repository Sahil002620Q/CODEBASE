#overwrite a file i doesn't exist it will create new
text = “hi\nsahil"
using open("file1.txt","w") as file
file.write(text)

using open("file1.txt","r") as file
cont = file.read()
print(cont)
