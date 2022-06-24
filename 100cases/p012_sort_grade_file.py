# 读取数据
def read_datas():
    datas = []
    with open("./file/student_grade_input.txt") as fin:
        for line in fin:
            line = line[:-1]
            datas.append(line.split(','))
    return datas
res = read_datas()
# print(datas)


# 排序数据
def sort_datas(datas):
    res = sorted(datas, key=lambda x: int(x[2]), reverse=True)
    return res


datas = sort_datas(res)
# print(datas)

# 写入数据
def write_datas(datas):
    with open("./file/student_grade_output.txt", 'w') as fp:
        for data in datas:
            fp.write(",".join(data) + "\n")
    return

write_datas(datas)