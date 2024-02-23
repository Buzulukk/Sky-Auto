import json
import pygame

import keyboardactivity as ka
import interface

pygame.init()
clock = pygame.time.Clock()

# FPS
divider = 60.0 
FPS = 1000/divider

def file_processing(file_path):
    success = False
    song = []
    
    # .txt -> str
    try:
        str_obj = open(file_path, "r", encoding='utf16').read()[1:-2]
        song = json.loads(str_obj) # str -> obj
        success = True
    except Exception as e:
        pass

    if not success:
        try:
            str_obj = open(file_path, "r", encoding='utf8').read()[1:-2]
            song = json.loads(str_obj) # str -> obj
            success = True
        except Exception as e:
            pass

    if not success:
        try:
            str_obj = open(file_path, "r", encoding='utf16').read()[1:-1]
            song = json.loads(str_obj) # str -> obj
        except Exception as e:
            pass

    if not success:
        try:
            str_obj = open(file_path, "r", encoding='utf8').read()[1:-1]
            song = json.loads(str_obj) # str -> obj
        except Exception as e:
            pass

    play_song(song)

def play_song(song):
    time_cnt = 0
    idx = 0

    try:
        while True:
            if interface.stop_thread.is_set():
                break
            
            ka.add_little_error()
            ka.clean_keys()        
            
            if (round(song["songNotes"][idx]["time"] / divider) == time_cnt):
                ka.play_note(song["songNotes"][idx]["key"])
                
                idx += 1
                if (round(song["songNotes"][idx]["time"] / divider) == time_cnt):
                    continue
                
            time_cnt += 1

            clock.tick(FPS)
    except Exception as e:
        pass

if __name__ == "__main__":
    interface.start()
