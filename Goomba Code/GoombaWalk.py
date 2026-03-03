import time
import os
import subprocess

class Goombawalk:
    def __init__(self, star, goomba, ground):
        self.__star = star
        self.__goomba = goomba
        self.__ground = ground
    
    def draw_frame(self):
        self.__star.draw_sprite()
        self.__goomba.draw_sprite()
        self.__ground.draw_sprite()

    def start_animation(self):
        frame_number = 20 #number of frames drawn
        sleep_time = 0.2 #time between frames
        for i in range(frame_number):
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) # Clear console using subprocess
            self.draw_frame()
            self.__goomba.update_pos()
            time.sleep(sleep_time) 

        self.__goomba.change_dir()
        self.__goomba.update_pos()

        for i in range(frame_number):
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) # Clear console using subprocess
            self.draw_frame()
            self.__goomba.update_pos()
            time.sleep(sleep_time) 