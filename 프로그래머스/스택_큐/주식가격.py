# https://programmers.co.kr/learn/courses/30/lessons/42586

pricesList = [
    [1, 2, 3, 2, 3]
]

returnList = [
    [4, 3, 1, 1, 0]
]


def solution(prices):
    pricesLen = len(prices)
    result = [0] * pricesLen

    for i in range(0, pricesLen):
        cnt = 0
        for j in range(i+1, pricesLen):
            cnt += 1
            if prices[i] > prices[j]:
                break

        result[i] = cnt

    return result


for p, r in zip(pricesList, returnList):

    result = solution(p)

    if result == r:
        print("성공")
    else:
        print("실패")
