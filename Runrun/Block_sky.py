from PIL import Image, ImageDraw

class Block_sky:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+60, position[1]+60))
        self.shape = Image.open("sky.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.position = position
      