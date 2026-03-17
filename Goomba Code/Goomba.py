class Goomba:
    def __init__(self, speed: int):
        self.__pos_x = 0
        self.__speed = speed
        self._goomba_sprite = [""] * 10
        self._set_sprite() #for setting goomba image to _goomba_sprite
        self.__direction = True #True: ->, False: <-

    def _set_sprite(self):
        self._goomba_sprite[0] = r"     ________  "
        self._goomba_sprite[1] = r"    /        \ "
        self._goomba_sprite[2] = r"   /  \    /  \ "
        self._goomba_sprite[3] = r"  /   |    |   \ "
        self._goomba_sprite[4] = r" /  -^------^-  \ "
        self._goomba_sprite[5] = r"|________________| "
        self._goomba_sprite[6] = r"      /    \ "
        self._goomba_sprite[7] = r" ____|      |____ "
        self._goomba_sprite[8] = r"/____\ ==== /____\ "
        self._goomba_sprite[9] = r"                     "
    
    def draw_sprite(self):
        spaces = " " * self.__pos_x
        for each_line in self._goomba_sprite:
            print(spaces + each_line)

    def update_pos(self):
        if self.__direction: #If self.__direction == True
            self.__pos_x += self.__speed
        else: #If self.__direction == False
            self.__pos_x -= self.__speed
    
    def change_dir(self):
        self.__direction = not self.__direction #Changes True to False and False to True