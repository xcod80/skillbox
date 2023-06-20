import datetime
from random import randint
class KillError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'Убийство!!! {self.message}'
        else:
            return 'Убийство!!!'
class DrunkError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'Наступило опьянение!!! {self.message}'
        else:
            return 'Наступило опьянение!!!'
class CarCrashError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'Автокатострофа!!! {self.message}'
        else:
            return 'Автокатастрофа!!!'
class GluttoryError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'Обожрался!!! {self.message}'
        else:
            return 'Обожрался!!!'
class DepressionError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'Депрессия!!! {self.message}'
        else:
            return 'Депрессия!!!'
class Life:
    __errors = [KillError, DrunkError, CarCrashError, GluttoryError, DepressionError]
    def __init__(self, maxkarma):
        self.__maxkarma = maxkarma
    def one_day(self):
        if randint(1, 10) == 10:
            raise self.__errors[randint(0, 4)]
        return randint(1, self.__maxkarma)
life = Life(7)
karma = 0
day = 1
while True:
    try:
        karma += life.one_day()
    except KillError:
        with open('karma.log', 'a') as logfile:
            logfile.write(str(datetime.datetime.now()) + ':День '+ str(day) + ':' + str(KillError()) + '\n')
    except DrunkError:
        with open('karma.log', 'a') as logfile:
            logfile.write(str(datetime.datetime.now()) + ':День '+ str(day) + ':' + str(DrunkError()) + '\n')
    except CarCrashError:
        with open('karma.log', 'a') as logfile:
            logfile.write(str(datetime.datetime.now()) + ':День '+ str(day) + ':' + str(CarCrashError()) + '\n')
    except GluttoryError:
        with open('karma.log', 'a') as logfile:
            logfile.write(str(datetime.datetime.now()) + ':День '+ str(day) + ':' + str(GluttoryError()) + '\n')
    except DepressionError:
        with open('karma.log', 'a') as logfile:
            logfile.write(str(datetime.datetime.now()) + ':День '+ str(day) + ':' + str(DepressionError()) + '\n')
    else:
        if karma > 500:
            print(f'Вы достигли просвветления на {day} день!!!')
            break
    day += 1