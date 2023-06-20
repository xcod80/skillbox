violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

numbers = ['первой', 'второй', 'третьей', 'четвертой', 'пятой', 'шестой', 'седьмой', 'восьмой', 'девятой']

total_time = 0
print('Песни в списке:', [song for song in violator_songs.keys()])
for i in range(int(input('Сколько песен выбрать?'))):
    while True:
        current_song = input(f'Название {numbers[i]} песни: ')
        if current_song in violator_songs.keys():
            total_time += violator_songs[current_song]
            break
print('Общее время звучания песен: {:2} минут'.format(total_time))