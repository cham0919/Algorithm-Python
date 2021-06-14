import collections

# https://programmers.co.kr/learn/courses/30/lessons/42576

participantList = [
    ["leo", "kiki", "eden"],
    ["marina", "josipa", "nikola", "vinko", "filipa"],
    ["mislav", "stanko", "mislav", "ana"]
]

completionList = [
    ["eden", "kiki"],
    ["josipa", "filipa", "marina", "nikola"],
    ["stanko", "ana", "mislav"]
]

returnList = [
    "leo",
    "vinko",
    "mislav"
]



def solution1(participants, completions):
    participants.sort()
    completions.sort()
    for i in range(0, len(completions), 1):
        if completions[i] != participants[i]:
            return participants[i]
    return participants.pop()


def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def solution3(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


for p, c, r in zip(participantList, completionList, returnList):

    result = solution1(p, c)

    if result == r:
        print("성공")
    else:
        print("실패")
