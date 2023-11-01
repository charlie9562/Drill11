from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE

import game_framework
from pico2d import load_image, delay, clear_canvas, update_canvas, get_events, get_time

def init():
    global image
    image = load_image('title.png')
    pass
def finish():
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass
def update():
    pass
def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass