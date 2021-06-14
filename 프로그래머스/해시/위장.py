# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
from collections import Counter

clothesList = [
    [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
]

returnList = [
    5,
    3
]


def solution1(clothes):
    result = 1;
    total_shares = Counter()
    for value, key in clothes:
        total_shares[key] = total_shares[key]+1
    for i in total_shares.values():
        result *= i+1
    return result-1


def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


for c, r in zip(clothesList, returnList):

    result = solution1(c)

    if result == r:
        print("성공")
    else:
        print("실패")
