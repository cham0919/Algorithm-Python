"""https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3"""

numberList = [
    "1924",
    "1231234",
    "4177252841",
    "1000"
]

kList = [
    2,
    3,
    4,
    1
]

returnList = [
    "94",
    "3234",
    "775841",
    "100"
]


def solution(number, k):
    answer = []
    cnt = k
    for n in number:
        while len(answer) > 0 and answer[-1] < n and cnt > 0:
            cnt -= 1
            answer.pop()

        answer.append(n)

    result = ''
    for i in range(len(number) - k):
        result += answer[i]

    return result



for n, k, r in zip(numberList, kList ,returnList):

    result = solution(n, k)

    if result == r:
        print("성공")
    else:
        print("실패")
