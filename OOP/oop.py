class student:
    def __init__(self, x, y, z):
        self.name = x
        self.stream = y
        self.rollno = z

    def info(self):
        print(f"{self.name} is studying {self.stream} and his roll number is {self.rollno}")

# create new list
a = student("sahil", "ai-ml", "624")
b = student("sam","bca","625")

# print list 
a.info()
b.info()