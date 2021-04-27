import time
import keyboard

songsFile = open('songs.txt', 'r')
songs = songsFile.read().splitlines()

print("Warte 5 Sekunden vor dem schreiben.")
for i in range(0, 5):
    print(5-i)
    time.sleep(1)

keyboard.write("/poll")
time.sleep(0.25)
keyboard.write("Bester Song? ")
time.sleep(0.25)
keyboard.press_and_release('tab')
time.sleep(0.25)

index = True
for song in songs:
    if index:
        index = not index
        continue
    else:
        index = not index

    keyboard.press_and_release('tab')
    time.sleep(0.25)
    keyboard.write(song)
    time.sleep(0.25)
    keyboard.press_and_release('tab')
    time.sleep(0.25)
    print("Song: " + song)
