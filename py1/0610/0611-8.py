students = {"111-34-3434": "John", "132-56-6290": "Peter"}
students["234-56-9010"] = "Susan"
print(students)

print(students["234-56-9010"])

students["111-34-3434"] = "John Smith"
print(students["111-34-3434"])

# print(students["343-45-5455"])

print(students)

print(tuple(students.keys()))
print(tuple(students.values()))

print(tuple(students.items()))

print(students.get("111-34-3434"))
students.pop("111-34-3434")


print(students)