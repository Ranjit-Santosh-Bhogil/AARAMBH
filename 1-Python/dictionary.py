student={
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science", "History"]
}
print(student)  # Output: {'name': 'John', 'age': 20, 'courses': ['Math', 'Science', 'History']}
print(student["name"])  # Output: John
print(student["courses"])  # Output: ['Math', 'Science', 'History']


student["age"] = 21
student["courses"].append("English")
print(student)  # Output: {'name': 'John', 'age': 21,

student.keys()  # Output: dict_keys(['name', 'age', 'courses'])
student.values()  # Output: dict_values(['John', 21, ['Math', '
student.items()  # Output: dict_items([('name', 'John'), ('age', 21), ('courses', ['Math', 'Science', 'History', 'English'])])

print(student.get("name","none"))  # Output: John
# if the key is not present, it will return the default value "none"
# helps to avoid KeyError when trying to access a key that may not exist in the dictionary.
