from ursina import *
import time
import random
import pyautogui
from ursina.prefabs.cursor import *

app = Ursina()

window.fps_counter.enabled=False
window.title=('Game Name')

player = FrameAnimation3d('assets/player/player_', texture='assets/player/texture',
                          double_sided=True, position=(0, 2, -2000),
                          scale=2, collider='box')
camera.z=-15
camera.add_script(SmoothFollow(target=player, offset=(0, 5, -30)))

road= Entity(model='plane',texture='grass', scale=(50, 10, 1000000), color=color.dark_gray)
rows= [-15 ,-10, -5, 0, 5, 10, 15]

median_right = Entity(model='cube', texture='grass', collider='box', position=(25, 2, 0),
                      scale=(5, 10, 1000000), color=color.white)
median_left = Entity(model='cube', texture='grass', collider='box', position=(-25, 2, 0),
                      scale=(5, 10, 1000000), color=color.white)

sky = Sky()
app.run()








