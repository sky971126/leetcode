import collections

def solution(userSongs, songGenres):
    song2Genre = {song:genre for genre, songs in songGenres.items() for song in songs}
    res = {}
    for person, songs in userSongs.items():
        genres2Count = collections.Counter([song2Genre[song] for song in songs])
        max_count = 0
        for genre, count in genres2Count.items():
            if max_count < count:
                max_count = count
                res[person] = [genre]
            elif max_count == count:
                res[person].append(genre)
    return res



userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}
print(solution(userSongs, songGenres))