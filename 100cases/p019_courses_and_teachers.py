teachers = {}
with open("./file/course_teachers.txt") as fp:
    for line in fp:
        line = line[:-1]
        course, teacher = line.split(',')
        teachers[course] = teacher

# print(teachers)

target_list = []
with open('./file/courses_students_grades.txt') as fp:
    for line in fp:
        line = line[:-1]
        line = line.split(',')
        target_list.append(line)

for x in target_list:
    x.append(teachers[x[0]])

with open('./file/course_scores_teachers.txt', 'w') as fp:
    for line in target_list:
        fp.write(','.join(line)+'\n')
