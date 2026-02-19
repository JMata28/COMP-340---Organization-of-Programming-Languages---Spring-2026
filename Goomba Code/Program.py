import Star, Goomba, Ground, GoombaWalk
import subprocess
import os

star = Star(0)
goomba = Goomba(4)
ground = Ground(120)

gWalkAnimation = GoombaWalk(star, goomba, ground)

# Clear console using subprocess
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

gWalkAnimation.start_animation()