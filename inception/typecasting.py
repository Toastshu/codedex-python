# typecasting means the process of converting a value from one data type to another data type.
# especially important handling with user input
name = "Eren" 
age = 19
height = 175.6
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(f"{name} is {age} years old")

height = int(height) #conversion from float to int
print(type(height))

age = str(age)
age += "1"
print(age)
print(type(age))

name = bool(name)



Output:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
Eren is 19 years old
<class 'int'>
191
<class 'str'>
