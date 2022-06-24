
def compute_scores():
    scores = []
    with open("./file/student_grade_input.txt") as fp:
        for line in fp:
            line = line[:-1]
            fileds = line.split(',')
            scores.append(int(fileds[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores) / len(scores), 2)
    return max_score, min_score, avg_score


max_score, min_score, avg_score = compute_scores()
print(f"max_score={max_score}, min_score={min_score}, avg_score={avg_score}")