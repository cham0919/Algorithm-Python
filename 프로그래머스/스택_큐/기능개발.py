# https://programmers.co.kr/learn/courses/30/lessons/42586
import math

progressesList = [
    [93, 30, 55],
    [95, 90, 99, 99, 80, 99]
]

speedsList = [
    [1, 30, 5],
    [1, 1, 1, 1, 1, 1]
]

returnList = [
    [2, 1],
    [1, 3, 2]
]


def solution(progresses, speeds):
    day = 0
    result = {}
    for p, s in zip(progresses, speeds):
        mok = math.ceil((100 - p) / s)
        day = day > mok and day or mok
        if (result.__contains__(day)):
            result[day] += 1
        else:
            result[day] = 1

    return list(result.values())


for p, l, r in zip(progressesList, speedsList, returnList):

    result = solution(p, l)

    if result == r:
        print("성공")
    else:
        print("실패")
