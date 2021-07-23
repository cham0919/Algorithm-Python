"""https://programmers.co.kr/learn/courses/30/lessons/42860"""
from collections import Counter

peopleList = [
    [70, 50, 80, 50],
    [70, 80, 50]
]

limitList = [
    100,
    100
]

returnList = [
    3,
    3
]


def solution(people, limit):
    answer = 0

    people.sort()
    i = 0
    j = len(people)-1

    while i <= j:
        if (people[i] + people[j]) <= limit:
            i += 1
            j -= 1
        else:
            j -= 1
        answer += 1

    return answer



for p, l, r in zip(peopleList, limitList, returnList):

    result = solution(p, l)

    if result == r:
        print("성공")
    else:
        print("실패")
