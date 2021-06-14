# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3



prioritiesList = [
    [2, 1, 3, 2],
    [1, 1, 9, 1, 1, 1]
]

locationList = [
    2,
    0
]

returnList = [
    1,
    5
]


def solution(priorities, location):

    sortedPriorities = priorities.copy()
    sortedPriorities.sort(reverse=True)
    result = 1

    while len(priorities) > 0:
        tmpElement = priorities.pop(0)
        if tmpElement < sortedPriorities[0]:
            priorities.append(tmpElement)
            location -= 1
        else:
            if location == 0:
                return result
            else:
                sortedPriorities.pop(0)
                result += 1
                location -= 1

        location = len(priorities)-1 if location < 0 else location


for p, l, r in zip(prioritiesList, locationList, returnList):

    result = solution(p, l)

    if result == r:
        print("성공")
    else:
        print("실패")
