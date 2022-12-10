from PIL import Image, ImageDraw

class Character_back:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+65, position[1]+65))
        self.shape = Image.open("basic.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.position = position

    def move(self, command = None):
        self.list = list(self.position)

        if command['move'] == False:
            self.state = None
        else:
            self.state = 'move'

            if command['up_pressed']:
                back = Image.open("background.png")
                slide = Character_Basic((0,130),back) #basic 114 / slide 130 / 
                back.paste(slide.shape,(slide.position[0], slide.position[1]))
                self.joystick.disp.image(back)