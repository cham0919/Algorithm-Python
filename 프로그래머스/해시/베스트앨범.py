# https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

genresList = [
    ["classic", "pop", "classic", "classic", "pop"]
]

playsList = [
    [500, 600, 150, 800, 2500]
]

returnList = [
    [4, 1, 3, 0]
]


def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic: dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)

    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer


class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play

    def __le__(self, other):
        return self.play <= other.play

    def __gt__(self, other):
        return self.play > other.play

    def __ge__(self, other):
        return self.play >= other.play

    def __eq__(self, other):
        return self.play == other.play

    def __ne__(self, other):
        return self.play != other.play


for g, p, r in zip(genresList, playsList, returnList):

    result = solution(g, p)

    if result == r:
        print("성공")
    else:
        print("실패")
