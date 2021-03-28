student_scores = input("Input a list of student scores ").split(", ")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
max_score = 0
min_score = 100
for score in student_scores:
    if score>=max_score:
        max_score=score
    elif score<=min_score:
        min_score=score

print(f"The highest score in the class is: {max_score}\nThe minimal score in the class is: {min_score}")
