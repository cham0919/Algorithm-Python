"""https://programmers.co.kr/learn/courses/30/lessons/42747?language=java#fn1"""

citationsList = [
    [3, 0, 6, 1, 5]
]

returnList = [
    3
]


def solution(citations):
    citations.sort()
    for v in range(0, len(citations), 1):
        h_index = len(citations) - v
        if h_index <= citations[v]:
                return h_index
    return 0

for c, r in zip(citationsList, returnList):

    result = solution(c)

    if result == r:
        print("성공")
    else:
        print("실패")
