"""https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3"""
from collections import Counter

routesList = [
    [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
]

returnList = [
    2
]


def solution(routes):
    routes = sorted(routes, key=lambda x: x[1]);
    result = 0
    cctv = -30000

    for s, e in routes:
        if cctv < s:
            cctv = e
            result += 1

    return result


for routesParma, r in zip(routesList, returnList):

    result = solution(routesParma)

    if result == r:
        print("성공")
    else:
        print("실패")
