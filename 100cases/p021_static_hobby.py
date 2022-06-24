hobbies_count = {}

with open('./file/students_hobby.txt') as fp:
    datas = []
    for line in fp:
        line = line[:-1]
        datas.append(line.split(' '))

    hobbies = []
    for data in datas:
        hobbies.append(data[1].split(','))

    for hobby in hobbies:
        for x in hobby:
            if x not in hobbies_count:
                hobbies_count[x] = 0
            hobbies_count[x] += 1
    print(hobbies_count)