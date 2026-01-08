
student_scores = [150, 142, 185, 320, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# done searching out the max score in this list via built in function
print(max(student_scores))


#find max score using for loop and conditional statems
max_score = student_scores[0]

for score in student_scores:
    if score > max_score:
        max_score = score

print("The highest score in this class list is: " +str(max_score))

