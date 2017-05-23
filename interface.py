import rendering
import gamecode
import errors

import sfml as sf

class Oldwood(object):
    def __init__(self, resolution=(640, 480), title="Oldwood"):
        self.window = sf.graphics.RenderWindow(sf.VideoMode(resolution[0], resolution[1], sf.VideoMode.get_desktop_mode().bpp), title)

    def loop(self):
        self.window.clear(sf.graphics.Color(0, 0, 255, 255))

        rendering.draw_all(self.window)

        for evt in iter(self.window.poll_event(), False):
            gamecode.game_do("__sfml_event__", evt)
