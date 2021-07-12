"""https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3"""
from collections import Counter

nList = [
    5,
    5,
    5
]

lostList = [
    [2, 4],
    [2, 4],
    [2, 3, 4]
]

reserveList = [
    [1, 3, 5],
    [3],
    [1, 2, 3]
]

returnList = [
    5,
    4,
    4
]


def solution(n, lost, reserve):
    answer = n
    student = [0 for i in range(0, n+2)]
    lostList = Counter(lost) - Counter(reserve)
    reserveList = Counter(reserve) - Counter(lost)

    for lost in lostList:
        student[lost] -= 1
        answer -= 1
    for reserve in reserveList:
        if reserve-1 > 0 and student[reserve-1] == -1:
            student[reserve-1] += 1
            answer += 1
        elif reserve+1 <= n and student[reserve+1] == -1:
            student[reserve+1] += 1
            answer += 1

    return answer



def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


for n, l, re, r in zip(nList, lostList, reserveList ,returnList):

    result = solution(n, l, re)

    if result == r:
        print("성공")
    else:
        print("실패")
