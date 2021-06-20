"""https://programmers.co.kr/learn/courses/30/lessons/42746"""

from functools import cmp_to_key

numbersList = [
    [6, 10, 2],
    [3, 30, 34, 5, 9]
]


returnList = [
    "6210",
    "9534330"
]


def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer


for n, r in zip(numbersList, returnList):

    result = solution(n)

    if result == r:
        print("성공")
    else:
        print("실패")
