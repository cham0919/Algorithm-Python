"""https://programmers.co.kr/learn/courses/30/lessons/42860"""
from collections import Counter

nameList = [
    "JEROEN",
    "JAN",
    "JAZ"
]

returnList = [
    56,
    23,
    11
]


def solution(name):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    nameArray = [n for n in name]
    min_distance = len(name) - 1;
    result = 0;
    next = 0;
    for i in range(0, len(name)):
        result += min(alphabet.index(nameArray[i]), len(alphabet) - alphabet.index(nameArray[i]))

        next += 1
        while next < len(nameArray) and nameArray[next] == 'A':
            next += 1

        min_distance = min(min_distance, i + i + len(nameArray) - next)

    result += min_distance

    return result


for n, r in zip(nameList, returnList):

    result = solution(n)

    if result == r:
        print("성공")
    else:
        print("실패")
