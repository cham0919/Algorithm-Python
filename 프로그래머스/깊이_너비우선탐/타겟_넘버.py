"""https://programmers.co.kr/learn/courses/30/lessons/43165?language=java"""

numbersList = [
    [1, 1, 1, 1, 1]
]

targetList = [
    3
]

returnList = [
    5
]


def dfs(numbers, target, sum, depth):
    if depth == len(numbers):
        if sum == target:
            return 1
        else:
            return 0

    return dfs(numbers, target, sum+numbers[depth], depth+1) + dfs(numbers, target, sum-numbers[depth], depth+1)


def solution(numbers, target):
    return dfs(numbers, target, 0, 0)


for n, t, r in zip(numbersList, targetList, returnList):

    result = solution(n, t)

    if result == r:
        print("성공", result, r)
    else:
        print("실패", result, r)
