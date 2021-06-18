"""https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3"""

arrayList = [
    [1, 5, 2, 6, 3, 7, 4]
]

commandsList = [
    [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
]

returnList = [
    [5, 6, 3]
]


def solution(arrayList, commandsList):
    result = []
    for i in commandsList:
        tempArray = sorted(arrayList[i[0] - 1:i[1]])
        result.append(tempArray[i[2] - 1])
    return result


for a, c, r in zip(arrayList, commandsList, returnList):

    result = solution(a, c)

    if result == r:
        print("성공")
    else:
        print("실패")
