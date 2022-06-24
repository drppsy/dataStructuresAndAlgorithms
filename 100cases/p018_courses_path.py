target_path = './file/courses_students_grades.txt'


# 读取数据

def get_datas():
    datas = []
    with open(target_path) as fp:
        for line in fp:
            line = line[:-1]
            datas.append(line.split(','))
    return datas
datas = get_datas()
# print(datas)


# 统计各学科和各学科的分数
def static_subject(datas):
    static_dict = {}
    for data in datas:
        if data[0] not in static_dict:
            static_dict[data[0]] = []
        static_dict[data[0]].append(int(data[3]))
    return static_dict

res = static_subject(datas)
# print(res)


# 统计各学科的最高分、最低分、平均分
def static_subject_scores(datas):
    statics_scores = {}
    for k, v in datas.items():
        scores = []
        max_score = max(v)
        min_score = min(v)
        avg_score = round(sum(v) / len(v), 2)
        scores.append(max_score)
        scores.append(min_score)
        scores.append(avg_score)
        statics_scores[k] = scores
    return statics_scores


for k, v in static_subject_scores(res).items():
    print(f"{k}的最高分是{v[0]}, 最低分是{v[1]}, 平均分是{v[2]}")
