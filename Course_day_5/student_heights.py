student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

count = 0
h_sum = 0
for h in student_heights:
    count += 1
    h_sum += h
sr_sum = round(h_sum/count)
print(sr_sum)
