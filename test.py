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
                          scale=2.5, collider='box')
camera.z=-15
camera.add_script(SmoothFollow(target=player, offset=(0, 5, -30)))

road= Entity(model='plane',texture='grass',texture_scale=(2,1) , scale=(50, 10, 1000000), color=color.dark_gray)
rows= [-15 ,-10, -5, 0, 5, 10, 15]

median_right = Entity(model='cube', texture='grass', collider='box', position=(25, 2, 0),
                      scale=(5, 10, 1000000), color=color.black50)
median_left = Entity(model='cube', texture='grass', collider='box', position=(-25, 2, 0),
                      scale=(5, 10, 1000000), color=color.black50)

speed = 200

def update():
    player.z = player.z + time.dt * speed
    global rows

    if held_keys['d']:
        player.x = player.x + time.dt * 25
    if held_keys['a']:
        player.x = player.x - time.dt * 25
    if held_keys['enter']:
        quit()

    if player.intersects().hit or median_right.intersects().hit or median_left.intersects().hit:
        camera.shake(duration=0.5)
        player.visible = False
        camera.fov = -10

for i in range(0, 100000, 100):
    enemy = Entity(model='assets/wall/barrier.obj', texture='assets/wall/barrierTX', y=-1,
                   rotation_y = 90, collider='box', position=(random.choice(rows), 3, i))
    enemy.scale = (3.5)

sky = Sky()
app.run()
