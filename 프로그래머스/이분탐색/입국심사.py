"""https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3"""

nList = [
    6
]

timesList = [
    [7, 10]
]

returnList = [
    28
]


def solution(n, times):
    times.sort()
    min = 1
    max = times[len(times)-1] * n
    answer = max

    while min <= max:
        sum = 0
        mid = int((min + max)/2)

        for t in times:
            sum += int(mid/t)

        if sum >= n:
            if mid < answer:
                answer = mid
            max = mid-1
        else:
            min = mid+1


    return answer


for n, t, r in zip(nList, timesList, returnList):

    result = solution(n, t)

    if result == r:
        print("성공")
    else:
        print("실패")
