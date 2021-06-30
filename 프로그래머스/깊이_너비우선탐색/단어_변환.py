"""https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3"""
import math
from collections import defaultdict

beginList = [
    "hit",
    "hit"
]

targetList = [
    "cog",
    "cog"
]

wordsList = [
    ["hot", "dot", "dog", "lot", "log", "cog"],
    ["hot", "dot", "dog", "lot", "log"]
]

returnList = [
    4,
    0
]


def isPossibleChange(target, val):
    result = 0
    for t, v in zip(target, val):
        if t != v:
            result += 1

    return result < 2


def dfs(resultArr, check, begin, target, count):
    if isPossibleChange(begin, target):
        resultArr[0] = min(resultArr[0], count+1)

    for idx, val in enumerate(resultArr[1:]):
        if check[idx]:
            continue
        if isPossibleChange(target, val):
            check[idx] = True
            dfs(resultArr, check, begin, val, count + 1)
            check[idx] = False


def solution(begin, target, words):
    if not words.__contains__(target):
        return 0

    resultArr = [len(words)] + words
    check = defaultdict(lambda: False)
    check[words.index(target)] = True
    dfs(resultArr, check, begin, target, 0)
    return resultArr[0]


for b, t, w, r in zip(beginList, targetList, wordsList, returnList):

    result = solution(b, t, w)

    if result == r:
        print("성공", result, r)
    else:
        print("실패", result, r)
