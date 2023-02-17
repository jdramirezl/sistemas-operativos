import os
import pygame
import time

def play_audio_file(file_path): 
    print("Playing: " + file_path)
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    length = pygame.mixer.Sound(file_path).get_length()
    print(f'Length: {length/60}')
    

    while pygame.mixer.music.get_busy():
        #Get the current position of the sound
        current_pos = pygame.mixer.music.get_pos()/1000

        # Calculate the progress of the sound
        progress = current_pos / length

        # Print the progress bar
        print("[{0: <30}] {1:.1f}%".format("=" * int(progress * 30), progress * 100))

        # Wait for a short time
        time.sleep(0.1)

def func():
    proc = os.fork()

    if proc < 0:
        print("fork failed")
        exit(1)
    elif proc == 0:
        print("hello, I am child (pid:{})".format(os.getpid()))
        while True:
            time.sleep(5)
            play_audio_file("ad.mp3")
    else:
        print("hello, I am parent of {} (pid:{})".format(proc, os.getpid()))
        play_audio_file("song.mp3")
        os.kill(proc, 9)

def main():
    func()

if __name__ == "__main__":
    main()
