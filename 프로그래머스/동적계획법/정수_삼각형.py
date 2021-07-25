"""https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3"""

triangleList = [
    [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
]


returnList = [
    30
]


def solution(triangle):
    for i in range(len(triangle)-2, -1, -1):
        layer = triangle[i]

        for ii in range(len(layer)):
            layer[ii] += max(triangle[i+1][ii], triangle[i+1][ii+1])

    return triangle[0][0]


for t, r in zip(triangleList, returnList):

    result = solution(t)

    if result == r:
        print("성공", result, r)
    else:
        print("실패", result, r)
