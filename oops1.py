# initiate a class

class employee:
    # Special/magic/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "engineer"

    def travel(self,destination):
        print(f"Employee is travalling to {destination}")


# Creating an object/instance of the class
sam  = employee()

# Printing an attribute 
print(sam.salary)

# calling a method 
sam.travel("keralam")

print(type(sam))
