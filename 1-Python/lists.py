lang=["Python", "Java", "C++", "JavaScript"]

print(lang[0])  # Output: Python
print(type(lang))  # Output: <class 'list'>


lang.append("Ruby")
lang.insert(2, "Go")
lang.remove("C++")
print(lang)  # Output: ['Python', 'Java', 'Go', 'JavaScript', 'Ruby']
lang[0] = "Python 3"

print(lang)  # Output: ['Python 3', 'Java', 'Go', 'JavaScript', 'Ruby']
print(lang[0])
print(lang[1:4])  # Output: ['Java', 'Go', 'JavaScript']