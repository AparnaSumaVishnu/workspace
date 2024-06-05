# # print("Hello World!")
# # print("I am learning Python")
# # #dynamic
# # x=10
# # y=3
# # z=x+y
# # print(z)
# # x="Appu"
# # print(x)
# '''This is 
#     a multiline comment'''
# """This is 
#     a multiline comment"""
# #type casting
# age="25"
# marks="45"
# #int,float
# m=int(marks)
# lab_marks=35
# total_marks=m+lab_marks
# x=int(True)
# print(x)
# x=int(55.48)
# print(x)
# # name="Aparna"
# # message="Hello "+name+", Good Morning"
# # print(message)
# #positional arguments
# student_name="Aparna"
# age=20
# # m="Hello, I am "+ student_name + ".I am" + str(age) + "years old"
# message_template="Hello, T am {s_name}. I am {a} years old"
# m=message_template.format(s_name=student_name,a=age)
# print(m)

# #f-string
# m=f"Hello, I am {student_name}. I am {age} years old"
# print(m)
# message1=m.capitalize()
# print(message1)
# message2=m.upper()
# print(message2)
# message3=m.lower()
# print(message3)
# message4=m.swapcase()
# print(message4)

# prod_name="Mens T-shirts"
# product=prod_name.count("h")
# print(product)
# product1=prod_name.find("h")
# print(product1)
# product2=prod_name.split(" ")
# print(product2)
# prod_name="Mens T-shirts and Women T-shirts"
# phone="0987654321"
# num=phone.isnumeric()
# print(num)
# prod_name="Mens T-shirts and Women T-shirts"
# phone="0987654321"
# employee_name="Ammu"
# alp=employee_name.isalpha()
# print(alp)
# prod_name="Mens T-shirts and Women T-shirts"
# phone="0987654321"
# employee_name="Ammu"
# password="jdcn162"
# pas=password.isalnum()
# print(alp)

# prod_name="Mens T-shirts"
# m=prod_name.startswith("Mens")
# print(m)
# prod_name="Mens T-shirts"
# m=prod_name.endswith("Mens")
# print(m)
# prod_name="Mens T-shirts"
# m=prod_name.count("Mens")
# print(m)

# Lists-collection,ordered,duplicate,mutable
students=["Aparna","Ammu","Appu"]
student_scores=[45,36,78]
#student_list=list(("Aparna","Ammu","Appu"))
# print(students)
# students[2]="Akku"
# students.append("Ambu")
# students.insert(2,"Ajju")
# students.remove("Ammu")
# student_scores.insert(0,64)
# students.pop(2)
# students.reverse()
# students.sort()
# student_scores.sort(reverse=True)
# print(len(students), students, student_scores)

#Tuple-immutable,ordered,duplicate
# students=("Ammu",)
# print(type(students))
# del students
# students2=tuple(("Achu","Kichu","Nichu"))
# student_scores=(50,45,36)
# print(student_scores,students,students2)

#Set-unordered, duplicates not allowed, changes allowed
students={"Aparna","Ammu","Akku"}

s_name="Ammu"
if_exist=s_name in students
print(if_exist)
students.add("Aju")
students.remove("Aparna")
print(students)
