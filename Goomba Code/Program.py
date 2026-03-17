from Star import Star
from ParaGoomba import ParaGoomba
from Goomba import Goomba
from Ground import Ground
from GoombaWalk import Goombawalk
import subprocess
import os
import time

star = Star(0)
goomba = Goomba(4) #Goomba has speed of 4
ground = Ground(120)

# for i in range(3):
#     subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) # Clear console using subprocess
#     goomba.draw_sprite()
#     goomba.update_pos()
#     time.sleep(0.3) # wait 0.3 seconds

# goomba.change_dir()
# goomba.update_pos()

# for i in range(3):
#     subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) # Clear console using subprocess
#     goomba.draw_sprite()
#     goomba.update_pos()
#     time.sleep(0.3) # wait 0.3 seconds

gWalkAnimation = Goombawalk(star, goomba, ground)

#Clear console using subprocess
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

gWalkAnimation.start_animation()


#PARAGOOMBA CODE 
# pGoomba = ParaGoomba(4)
# pGoomba.draw_sprite()

# star = Star(0)
# ground = Ground(120)
# pGoomba = ParaGoomba(4)
# gWalkAni = Goombawalk(star, pGoomba, ground)

# #Clear console using subprocess
# subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
# gWalkAni.start_animation()