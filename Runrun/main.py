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
from time import time



def main():
    joystick = Joystick()
    back = Image.open("background.png")
    basic = Character_basic((0,114),back) #basic 114 / slide 130 / hi 80 / small 119
    back.paste(basic.shape,(basic.position[0], basic.position[1]))
    joystick.disp.image(back)
    mode1 = np.random.randint(0,2,50).tolist()
    mode2 = np.random.randint(0,2,100).tolist()
    time = 0
    block_out = 0
    flag = 0
    where_block = [1,2]
    basic_ = Character_basic((0,114),back)

    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False,
        'btn_A': False, 'btn_B': False}

        if not joystick.button_U.value: # 조이스틱 인식 부분
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

        if block_out == 0:
            fireflag = random.choice(where_block) # 불의 위치를 조정하기 위해 랜덤으로 0,1 추출
            if fireflag == 1: #fire가 0이면 바닥에 있는 불을 출력
                fire = Block_small((180,119),back) #basic 114 / slide 130 / hi 80 / small 119
                back.paste(fire.shape,(fire.position[0], fire.position[1]))
                joystick.disp.image(back)
                block_out = 1
                time += 1
              
            elif fireflag == 2: # fire가 1이면 공중에서 불이 날라온다.
                block_out = 1
                fire = Block_sky((180,80),back)
                back.paste(fire.shape,(fire.position[0], fire.position[1]))
                joystick.disp.image(back)
                time += 1

        flag, block_out = basic.move(back, flag, fireflag, fire, block_out, basic_, command)
        


if __name__ == '__main__':
    main()