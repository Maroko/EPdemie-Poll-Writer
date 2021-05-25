try:
    import time
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'time'])
    import time
try:
    import keyboard
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'keyboard'])
    import keyboard
try:
    import pyperclip
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'pyperclip'])
    import pyperclip

writeToFile = True
poll_text = ""


def write_poll(text_to_append, full_text):
    full_text = full_text + text_to_append
    return full_text


songsFile = open('songs.txt', 'r', encoding='utf8')
songs = songsFile.read().splitlines()

result = open("result.txt", "w", encoding='utf8')

poll_text = write_poll("/poll ", poll_text)
poll_text = write_poll("question:", poll_text)
poll_text = write_poll("Bester Song? ", poll_text)

skipSongNumber = input("Skip every second line (song number)? (y/n)")
if skipSongNumber == "y":
    skipSongNumber = True
else:
    skipSongNumber = False

index = True
index_char = 97
for song in songs:
    if skipSongNumber:
        if index:
            index = not index
            continue
        else:
            index = not index

    poll_text = write_poll("choice_" + chr(index_char) + ":", poll_text)
    poll_text = write_poll(song + " ", poll_text)
    print("Song: " + song)
    index_char = index_char + 1

print(poll_text)
answer = input("Write to file? (y/n)")
if answer == "y":
    result.write(poll_text)

answer = input("Write to keyboard? (y/n)")
if answer == "y":
    print("Warte 5 Sekunden vor dem schreiben.")
    for i in range(0, 5):
        print(5 - i)
        time.sleep(1)
    keyboard.write(poll_text)

answer = input("Copy to clipboard? (y/n)")
if answer == "y":
    pyperclip.copy(poll_text)
