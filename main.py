from pygame import mixer
import time


def getdate():
    import datetime
    return datetime.datetime.now()


print("Press any key to start the timer.")
a = input()
second = 0
while second <= 28800:
    time.sleep(1)
    second += 1
    if second % 1680 == 0:
        mixer.init()
        mixer.music.load("water.mp3")
        mixer.music.set_volume(1)
        mixer.music.play(100)
        while True:
            print("Type 'drank' to stop.")
            query = input("  ")
            if query.lower() == "drank":
                mixer.music.pause()
                f = open("Water.txt", "a")
                f.write(str([str(getdate())]))
                f.write("Drank water")
                f.write("\n")
                f.close()
            break
    if second % 1800 == 0 and second % 2700 != 0:
        mixer.init()
        mixer.music.load("eyes.mp3")
        mixer.music.set_volume(1)
        mixer.music.play(100)
        while True:
            print("Type 'Eydone' to stop.")
            query = input("  ")
            if query.lower() == "eydone":
                mixer.music.pause()
                f = open("Eyes.txt", "a")
                f.write(str([str(getdate())]))
                f.write("Eyes Done")
                f.write("\n")
                f.close()
            break
    if second % 2700 == 0 and second % 1800 != 0:
        mixer.init()
        mixer.music.load("exercise.mp3")
        mixer.music.set_volume(1)
        mixer.music.play(100)
        while True:
            print("Type 'Exdone' to stop.")
            query = input("  ")
            if query.lower() == "exdone":
                mixer.music.pause()
                f = open("Exercise.txt", "a")
                f.write(str([str(getdate())]))
                f.write("Exercise Done")
                f.write("\n")
                f.close()
                break
    print('\n\n\n\n\n\n\n')
    print('\t\t\t\t-------------')
    print('\t\t\t\t  %d '%(second))
    print('\t\t\t\t-------------')

