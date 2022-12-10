from PIL import Image, ImageDraw

class Block_small:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+30, position[1]+60))
        self.shape = Image.open("small.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.position = position
    