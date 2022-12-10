from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageOps, ImageFilter
import random
import numpy as np
from colorsys import hsv_to_rgb
from Joystick import Joystick
from Character_basic import Character_basic
from Character_slide import Character_slide
from Character_angry import Character_angry
from Block_sky import Block_sky
from Block_small import Block_small


def main():
    joystick = Joystick()
    back = Image.open("background.png")
    basic = Character_basic((0,114),back) #basic 114 / slide 130 / hi 80 / small 119
    back.paste(basic.shape,(basic.position[0], basic.position[1]))
    joystick.disp.image(back)
    mode1 = np.random.randint(0,2,50).tolist()
    mode2 = np.random.randint(0,2,100).tolist()
    time = 0
    block = [0,1]

    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False,
        'btn_A': False, 'btn_B': False}

        if not joystick.button_U.value:
            command['up_pressed'] = True
            command['move'] = True


        if not joystick.button_D.value:
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value: 
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value: 
            command['right_pressed'] = True
            command['move'] = True
        
        if not joystick.button_A.value:
            command['btn_A'] = True
            command['move'] = True
            

        if not joystick.button_B.value:
            command['btn_B'] = True
            command['move'] = True

        fire = random.choice(block)
        if fire == 0:
            small = Block_small((100,119),back) #basic 114 / slide 130 / hi 80 / small 119
            back.paste(small.shape,(small.position[0], small.position[1]))
            joystick.disp.image(back)
        else:
            sky = Block_sky((100,80),back)
            back.paste(sky.shape,(sky.position[0], sky.position[1]))
            joystick.disp.image(back)

        basic.move(back, command)


if __name__ == '__main__':
    main()