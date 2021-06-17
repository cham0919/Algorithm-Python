import heapq

# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3


operationsList = [
    ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],
    ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
]

returnList = [
    [0, 0],
    [333, -45]
]


def solution(operations):
    answer = [0, 0]
    queue = []
    reverseQueue = []

    for i in operations:
        str = i.split(" ")
        if str[0] == 'I':
            heapq.heappush(queue, int(str[1]))
            heapq.heappush(reverseQueue, int(str[1]) * -1)
        elif len(queue) > 0:
            if str[1] == '1':
                queue.remove(heapq.heappop(reverseQueue) * -1)
            else:
                reverseQueue.remove(heapq.heappop(queue) * -1)

    if len(queue) > 0:
        answer[0] = heapq.heappop(reverseQueue) * -1
        answer[1] = heapq.heappop(queue)

    return answer


for o, r in zip(operationsList, returnList):

    result = solution(o)

    if result == r:
        print("성공")
    else:
        print("실패")
