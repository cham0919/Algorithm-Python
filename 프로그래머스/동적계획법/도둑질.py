"""https://programmers.co.kr/learn/courses/30/lessons/42897?language=java"""
import math

moneyList = [
    [1, 2, 3, 1]
]

returnList = [
    4
]


def solution(money):
    dp = [0 for i in range(len(money)-1)]
    dp2 = [0 for i in range(len(money))]

    dp[0] = dp[1] = money[0]
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-2]+money[i], dp2[i-1])

    return max(dp[len(money)-2], dp2[len(money)-1])


def solution2(a):
    x1, y1, z1 = a[0], a[0], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)


for m, r in zip(moneyList, returnList):

    result = solution2(m)

    if result == r:
        print("성공", result, r)
    else:
        print("실패", result, r)
