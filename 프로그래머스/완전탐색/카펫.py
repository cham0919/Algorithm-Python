"""https://programmers.co.kr/learn/courses/30/lessons/42842?language=java"""

brownList = [
    10,
    8,
    24
]


yellowList = [
    2,
    1,
    24
]

returnList = [
    [4, 3],
    [3, 3],
    [8, 6]
]


def getDivisorSet(yellow):
    divisorSet = set()
    for v in range(1, int(yellow/2+2)):
        if yellow % v == 0:
            divisorSet.add((v, int(yellow/v)))
    return divisorSet


def solution(brown, yellow):
    # 약수
    divisorSet = getDivisorSet(yellow)
    # 둘레 구하기
    for a, b in divisorSet:
        if (2*(a+b)+4) == brown:
            result = [a+2, b+2]
            result.sort(reverse=True)
            return result



for b, y, r in zip(brownList, yellowList, returnList):

    result = solution(b, y)

    if result == r:
        print("성공")
    else:
        print("실패")
