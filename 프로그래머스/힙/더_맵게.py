import heapq

# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3


scovilleList = [
    [1, 2, 3, 9, 10, 12]
]

kList = [
    7
]

returnList = [
    2
]


def mixScoville(minScoville, heap):
    minSecondScoville = heapq.heappop(heap)
    heapq.heappush(heap, (minScoville + (2 * minSecondScoville)))


def solution(s, k):
    answer = 1
    scovilleLen = len(s)
    heapq.heapify(s)
    minScoville = heapq.heappop(s)


    for i in range(0, scovilleLen - 1):
        mixScoville(minScoville, s)
        minScoville = heapq.heappop(s)
        if minScoville >= k:
            return answer
        answer += 1

    return -1


for c, k, r in zip(scovilleList, kList, returnList):

    result = solution(c, k)

    if result == r:
        print("성공")
    else:
        print("실패")
