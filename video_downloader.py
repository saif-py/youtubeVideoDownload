import pafy
import sys
import threading
import time


def animated_loading():
    chars = "/—\|"
    for char in chars:
        sys.stdout.flush()
        sys.stdout.write('\r' + 'downloading video...' + char)
        time.sleep(.25)
        sys.stdout.flush()
        sys.stdout.write('\r' + " ")


try:
    youtube_video_url = input("link :->")
    sys.stdout.write('\rgetting video info')
    vide_info = pafy.new(youtube_video_url)
    sys.stdout.write('\r' + vide_info.title)

    n = 1

    for i in vide_info.streams:
        print(f"\n{n}-> {i}")
        n += 1
    index = int(input("enter the downloading format: "))
    index = index - 1
    streams = vide_info.allstreams
    stream = streams[index]
    # getting file size of stream
    value = stream.get_filesize()

    # printing the value
    print("File Size in bytes: " + str(value))
    quality = vide_info.streams[index]


    def the_process_function():

        quality.download()
        sys.stdout.write('\r' + 'video downloaded')
        print(" ")


    the_process = threading.Thread(name='process', target=the_process_function)
    the_process.daemon = True
    the_process.start()
    while the_process.isAlive():
        animated_loading()
except Exception as e:
    print(e)
