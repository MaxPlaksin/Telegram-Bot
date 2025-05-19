import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(f'Осталось: {timeformat}', end='\r')
        time.sleep(1)
        seconds -= 1

    print("⏰ Время вышло!")

# Пример: запустить таймер на 1 минуту (60 секунд)
countdown_timer(60)
