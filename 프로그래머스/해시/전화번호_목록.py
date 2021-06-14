
# https://programmers.co.kr/learn/courses/30/lessons/42577

phoneBookList = [
    ["119", "97674223", "1195524421"],
    ["123", "456", "789"],
    ["12", "123", "1235", "567", "88"]
]

returnList = [
    False,
    True,
    False
]



def solution(phone_book):
    phone_book = sorted(phone_book)
    for phone, phone1 in zip(phone_book, phone_book[1:]):
        if(phone1.startswith(phone)):
            return False
    return True


for p, r in zip(phoneBookList, returnList):

    result = solution(p)

    if result == r:
        print("성공")
    else:
        print("실패")
