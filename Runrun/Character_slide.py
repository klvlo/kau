from PIL import Image, ImageDraw

class Character_slide:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+65, position[1]+65))
        self.shape = Image.open("slide.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.position = position