import pickle
import os

def input_scores():
    i = 0
    scores = []
    while True:
        i += 1
        score = int(input(f'#{i}? '))
        if score < 0:
            break
        scores.append(score)
    return scores

def get_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def save_scores(scores):
    with open("score.bin", "wb") as file:
        pickle.dump(scores, file)

def load_scores():
    if os.path.exists("score.bin"):
        with open("score.bin", "rb") as file:
            scores = pickle.load(file)
            return scores
    return None

def print_scores(scores):
    print("[점수 출력]")
    print("개인점수:", end=" ")
    for score in scores:
        print(score, end=" ")
    print()
    average = get_average(scores)
    print("평균:", average)

loaded_scores = load_scores()
if loaded_scores is None:
    print("[점수 입력]")
    scores = input_scores()
    save_scores(scores)
else:
    print("[파일 읽기]")
    scores = loaded_scores

print_scores(scores)
