import math

priorities = [2, 1, 3, 2]
# priorities = [1, 1, 9, 1, 1, 1]
location = 2
# location = 0

def solution(priorities, location):

    sortedPriorities = priorities.copy()
    sortedPriorities.sort(reverse=True)
    result = 1

    while len(priorities) > 0:
        tmpElement = priorities.pop(0)
        if tmpElement < sortedPriorities[0]:
            priorities.append(tmpElement)
            location -= 1
        else:
            if location == 0:
                return result
            else:
                sortedPriorities.pop(0)
                result += 1
                location -= 1

        location = len(priorities)-1 if location < 0 else location





print(solution(priorities, location))
