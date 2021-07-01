"""https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3"""
from collections import defaultdict
from itertools import groupby


ticketsList = [
    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]],
    [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]
]

returnList = [
    ["ICN", "JFK", "HND", "IAD"],
    ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],
    ["ICN", "SFO", "ICN", "SFO", "QRE"]
]


def dfs(ticketsMap, answer, nextPlace, idx):
    answer[idx] = nextPlace

    if idx == len(answer)-1:
        return -1

    for p in ticketsMap[nextPlace]:
        if not p[1]:
            p[1] = True
            if dfs(ticketsMap, answer, p[0], idx+1) < 0:
                return -1
            p[1] = False
    return 1


def solution(tickets):
    answer = ["" for i in range(len(tickets)+1)]
    ticketsMap = defaultdict(lambda: []);
    for ticket in tickets:
        ticketsMap[ticket[0]].append([ticket[1], False])

    for k, v in ticketsMap.items():
        v.sort(key = lambda x : x[0])

    dfs(ticketsMap, answer, "ICN", 0)

    return answer


for t, r in zip(ticketsList, returnList):

    result = solution(t)

    if result == r:
        print("성공", result, r)
    else:
        print("실패", result, r)
