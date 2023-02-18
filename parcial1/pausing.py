import os
import pygame
import time
import signal

def handler(sig, frame):
    print("Process killed")
    exit(1)

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
        print("\n[{0: <30}] {1:.1f}%".format("=" * int(progress * 30), progress * 100), end='\r')

        # Wait for a short time
        time.sleep(0.1)

def func():
    parent_pid = os.getpid()
    child = os.fork()

    signal.signal(signal.SIGINT, handler)

    if child < 0:
        print("fork failed")
        exit(1)
    elif child == 0:
        signal.signal(signal.SIGINT, handler)
        print("hello, I am child (pid:{})".format(os.getpid()))
        
        while True:
            time.sleep(5)
            os.kill(parent_pid, signal.SIGSTOP)
            play_audio_file("ad.mp3")
            os.kill(parent_pid, signal.SIGCONT)
    else:
        signal.signal(signal.SIGINT, handler)
        print("hello, I am parent of {} (pid:{})".format(child, os.getpid()))
        play_audio_file("song.mp3")
        os.kill(child, 9)

def main():
    func()

if __name__ == "__main__":
    main()
