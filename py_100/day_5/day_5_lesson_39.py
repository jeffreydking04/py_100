# Lesson 39: Highest Score

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65]

total = sum(student_scores)
print(total)

my_total = 0
for score in student_scores:
    my_total += score

print(my_total)

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
