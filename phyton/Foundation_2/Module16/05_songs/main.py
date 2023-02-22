violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
song_name = ''
song_time =0.0

def song_in_list(song, song_list):
    for cur_song in song_list:
        if cur_song[0] == song:
            return True
    return False

for song in violator_songs:
    print(song[0])
song_num = int(input("Сколько песен выбрать? "))
for i in range(song_num):
    while not song_in_list(song_name, violator_songs):
        song_name = input(f'Название {i+1}-ой песни: ')
    for song_cur in violator_songs:
        if song_name == song_cur[0]:
            song_time += song_cur[1]
    song_name = ''
print(f'Общее время звучания песен: {song_time} минуты')