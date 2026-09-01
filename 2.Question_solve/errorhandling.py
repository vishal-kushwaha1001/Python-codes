class MarksError(Exception):
    def __init__(self, marks):
        self.marks = marks

    def __str__(self):
        return f"Invalid marks: {self.marks}. Marks must be between 0 and 100."

try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise MarksError(marks)
    print("Marks accepted")
except MarksError as e:
    print(e)
