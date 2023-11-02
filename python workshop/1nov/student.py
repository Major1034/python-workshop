student={
   "name":"Alice",
   "age":25,
   "grade":"a"
}

student["city"]="new york"
#print(student)
#for key,value in student.items():
   #print(f"{key}:{value}")
# del student["age"]
# print(student)
student.update({"name":"anuj"})
print(student)
