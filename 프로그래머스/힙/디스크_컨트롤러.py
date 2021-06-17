import heapq
from collections import deque

"""
https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3
"""



jobsList = [
    [[0, 3], [1, 9], [2, 6]],
    [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
]



returnList = [
    9,
    74
]


def solution1(jobs):
    queue = []
    jobs.sort(key=lambda x : x[0])

    total = 0
    currentJobIdx = 0
    currentTime = 0

    while currentJobIdx < len(jobs) or len(queue) > 0:
        for i in range(currentJobIdx, len(jobs)):
            if jobs[i][0] <= currentTime:
                heapq.heappush(queue, jobs[i])
                currentJobIdx += 1
            else:
                break

        queue.sort(key=lambda x : x[1])

        if len(queue) == 0:
            currentTime += 1
            continue
        else:
            job = heapq.heappop(queue)
            currentTime += job[1]
            total += (currentTime-job[0])

    return total//len(jobs)


def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)


for j, r in zip(jobsList, returnList):

    result = solution1(j)

    if result == r:
        print("성공")
    else:
        print("실패")
