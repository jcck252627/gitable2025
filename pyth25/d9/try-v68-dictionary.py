# dictionary is a data structure that store key/value pair table

# mydictionary={"banana":"fruits","soda":"beverages"}

"""
print(mydictionary["banana"])
print(mydictionary["soda"])

mydictionary["dog"] = "animals"
mydictionary["cat"] ="animals"
mydictionary["chair"] ="furnitures"

print(mydictionary)
mydictionary["cat"] ="cute"
print(mydictionary)
"""
"""
for things in mydictionary:
    print(things)
    print(mydictionary[things])
"""

# coding exercise after v68

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}   # <-- use dictionary, not list

for name in student_scores:
    score = student_scores[name]

    if score >= 91:
        student_grades[name] = "Outstanding"
    elif score >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)




"""
    if student_scores[names] <=100 or student_scores[names] >=91:
        student_grades[student_scores[name] == "Outstanding"
    elif student_scores[names] <= 90 or student_scores[names] >=91:
         student_grades[student_scores[name] == "Exceeds Expectations"
"""