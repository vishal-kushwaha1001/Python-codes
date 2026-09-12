class student :
    
    # it initialized the object of  class student
    def __init__(self, name , rollNo , branch ):
        self.name = name 
        self.rollNo = rollNo
        self.branch = branch
        
    def display(self):
        print(f"Student Name is : {self.name} \nBranch is : {self.branch} \nAnd Roll No is : {self.rollNo} ")


s1 = student("Vishal Kushwaha", 62 , "MCA")
s2 = student("Anant Sagar", 11 , "MCA")


s1.display()

s2.display()
