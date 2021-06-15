# https://programmers.co.kr/learn/courses/30/lessons/42583
import collections

bridgeLengthList = [
    2,
    100,
    100
]

weightList = [
    10,
    100,
    100
]

truckWeightList = [
    [7, 4, 5, 6],
    [10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
]

returnList = [
    8,
    101,
    110
]


def solution1(bridge_length, weight, truck_weights):
    currentBridgeWeight = 0
    currentTruckIdx = 0
    answer = 0

    bridge = deque([0 for i in range(0, bridge_length)]);

    while currentTruckIdx < len(truck_weights):

        # moveOneBlock
        outTruck = bridge.pop()
        if outTruck > 0:
            currentBridgeWeight -= outTruck
        bridge.appendleft(0)
        answer += 1

        if currentTruckIdx >= len(truck_weights):
            pass
        elif bridge.index(0) > 0:
            pass
        else:
            if (currentBridgeWeight + truck_weights[currentTruckIdx]) <= weight:
                #         addTrcuk
                newTruck = truck_weights[currentTruckIdx]
                bridge[0] = newTruck
                currentBridgeWeight += newTruck
                currentTruckIdx += 1

    answer += bridge_length
    return answer



DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution2(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


for b, w, t, r in zip(bridgeLengthList, weightList, truckWeightList, returnList):

    result = solution2(b, w, t)

    if result == r:
        print("성공")
    else:
        print("실패")
