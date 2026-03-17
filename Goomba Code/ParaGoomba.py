from Goomba import Goomba

class ParaGoomba(Goomba):
    def __init__(self, speed):
        super().__init__(speed)   # calls Goomba constructor
        self._set_sprite()

    def _set_sprite(self):  # protected in ParaGoomba
        sprite = self._goomba_sprite  # access parent’s variable

        sprite[0] = r"              ________  "
        sprite[1] = r"             /        \ "
        sprite[2] = r"            /  \    /  \ "
        sprite[3] = r"           /   |    |   \ "
        sprite[4] = r"_________ /  -^------^-  \ _________"
        sprite[5] = r"\_       |________________|       _/"
        sprite[6] = r"  \_           /    \           _/  "
        sprite[7] = r"    \____ ____|      |____ ____/"
        sprite[8] = r"         /____\ ==== /____\ "
        sprite[9] = r"                             "