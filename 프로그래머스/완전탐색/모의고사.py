"""https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3"""

answersList = [
    [1, 2, 3, 4, 5],
    [1, 3, 2, 4, 2]
]

returnList = [
    [1],
    [1, 2, 3]
]


def solution(answers):
    answer = []
    answer1 = [1, 2, 3, 4, 5]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result1 = 0
    result2 = 0
    result3 = 0

    for i in range(0, len(answers), 1):
        if answer1[i % 5] == answers[i]: result1 += 1
        if answer2[i % 8] == answers[i]: result2 += 1
        if answer3[i % 10] == answers[i]: result3 += 1

    maxValue = max(result1, result2, result3)

    if maxValue == result1: answer.append(1)
    if maxValue == result2: answer.append(2)
    if maxValue == result3: answer.append(3)

    answer.sort()

    return answer


for a, r in zip(answersList, returnList):

    result = solution(a)

    if result == r:
        print("성공")
    else:
        print("실패")
