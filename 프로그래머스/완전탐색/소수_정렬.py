"""https://programmers.co.kr/learn/courses/30/lessons/42839"""

import math

numbersList = [
    "17",
    "011"
]

returnList = [
    3,
    2
]


def permutation(idxArray, depth, array, strArry, primeSet):
    for i in range(len(strArry)):
        if idxArray[i] == 1:
            continue
        array[depth] = strArry[i]
        if depth == len(array) - 1:
            num = ''
            for n in array:
                num += n
            primeSet.add(int(num))
        else:
            idxArray[i] = 1
            permutation(idxArray, depth + 1, array, strArry, primeSet)
            idxArray[i] = 0


def is_prime_number(x):
    if x < 2 or (x != 2 and x % 2 == 0):
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    primeSet = set()
    strArry = [*numbers]
    result = 0

    for i in range(len(numbers)):
        idx = [0 for n in range(len(numbers))]
        array = [0 for n in range(i + 1)]
        permutation(idx, 0, array, strArry, primeSet)

    for v in primeSet:
        if is_prime_number(v):
            print(v)
            result += 1

    return result


for n, r in zip(numbersList, returnList):

    result = solution(n)

    if result == r:
        print("성공")
    else:
        print("실패")
