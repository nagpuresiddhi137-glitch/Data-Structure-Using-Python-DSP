print("=====Student Data System======")


name=input("Enter Student Name:")
roll_no=int(input("Enter Student Roll No:"))
age=int(input("Enter Student Age:"))
marks=int(input("Enter Makrks:"))
is_pass=marks>=40

percentage=(marks/100)*100

print("\n===== Student Details ======")
print("Name:",name)
print("Roll No:",roll_no)
print("Marks:",marks)
print("Percentage:",percentage)
print("Result","Pass"if is_pass else "Fail")

print("\n====== Data Types Used=======")
print("Type of name:",type(name))
print("Type of roll_no:",type(roll_no))
print("Type of age:",type(age))
print("Type of marks:",type(marks))
print("Type of is_pass:",type(is_pass))




