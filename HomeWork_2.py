from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, skils, event_for_wait, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skils = skils
        self.event_for_wait = event_for_wait

    def run(self):

        print(f'{self.name}, на нас напали!')
        warriors = 100
        day = 0
        while warriors > 0:
            day = day + 1
            warriors = warriors - self.skils
            print(f"{self.name}, сражается {day} день(дня)..., осталось {warriors} воинов.")
            time.sleep(1)
        print(f"{self.name} отдержал победу спустя {day} дней")
if __name__ == "__main__":
    ruslan = Knight(name="Ruslan", skils= 20, event_for_wait=0)
    azat = Knight(name="Azat", skils =10, event_for_wait= 0)
    print('.' * 20)
    ruslan.start()
    azat.start()
    print('.' * 20)
    ruslan.join()
    azat.join()

    print('.' * 20, 'Все битвы закончились!')