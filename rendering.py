import sfml as sf

drawn = []
bgs = []

def drawsprite(o):
    return o.__sf_sprite__()

class Renderable(object):
    def __init__(self, t, props):
        self.t = t
        self.shown = None
        self.draw_index = None
        self.props = props

    def __setitem__(self, k, v):
        self.props[k] = v

    def __getitem__(self, k):
        return self.props[k]

    def __delitem__(self, k):
        del self.props[k]

    def show(self):
        global drawn

        if self.shown is None:
            self.shown = sf.graphics.Sprite(self.t)

            self.draw_index = len(drawn)
            drawn.append(self)

    def hide(self):
        self.shown = None

        drawn.pop(self.draw_index)
        self.draw_index = None

    def pre_draw(self, window):
        if self.shown is not None:
            for k, v in self.props.iteritems():
                setattr(self.shown, k, v)

        return self.shown is not None

    def reorder(self, i):
        shown.insert(i, shown.pop(self.draw_index))
        oi = self.draw_index
        self.draw_index = i

        return oi # Returns the old index

    def draw(self, window):
        window.draw(drawsprite(self))

    def post_draw(self, window):
        pass

    def __sf_sprite__(self):
        return self.shown

class Background(object):
    def __init__(self, img):
        self.tex = sf.graphics.Texture.from_file(img)

        bgs.append(self)

    def sf_image(self):
        return self.tex.to_image()

class BackgroundLayer(Renderable):
    def __init__(self, bgindex, x, y):
        self.imi = bgindex
        self.x = x
        self.y = y

    def pre_draw(self, window):
        if self.shown is not None:
            self.shown.position = sf.system.Vector2(self.x, self.y)
            self.shown.ratio = self.t

def draw_all(wind):
    for rd in drawn:
        if rd.pre_draw(wind):
            wind.draw(drawsprite(rd))
            rd.post_draw(wind)
            