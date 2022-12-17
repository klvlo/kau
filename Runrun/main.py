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
from Character_sweet import Character_sweet



def main():
    joystick = Joystick()
    back = Image.open("background.png") # 배경이미지 선언
    basic = Character_basic((0,114),back) # 기본 캐릭터 선언
    back.paste(basic.shape,(basic.position[0], basic.position[1])) # 캐릭터를 배경과 합치기
    joystick.disp.image(back) # 게임 화면 출력
    time = random.randint(10,20) # 장애물 개수를 10~20 사이로 랜덤하게 설정
    block_out = 0 # 장애물이 나온 상태인지 아닌지 확인
    flag = 0 # 캐릭터의 상태를 확인
    where_block = [1,2] # 장애물이 공중인지 바닥인지 정하기 위한 리스트
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

        if time > 0: # 만약 남은 장애물이 1개 이상일 때
            if block_out == 0: #블락이 나와있지 않다면
                fireflag = random.choice(where_block) # 불의 위치를 조정하기 위해 랜덤으로 0,1 추출
                if fireflag == 1: #fireflag 가 0이면 바닥에 있는 불을 출력
                    fire = Block_small((180,119),back) 
                    back.paste(fire.shape,(fire.position[0], fire.position[1]))
                    joystick.disp.image(back)
                    block_out = 1
                    
                
                elif fireflag == 2: # fire가 1이면 공중에서 불이 날라온다.
                    block_out = 1
                    fire = Block_sky((180,80),back)
                    back.paste(fire.shape,(fire.position[0], fire.position[1]))
                    joystick.disp.image(back)
        
        else: # 모든 장애물을 피했을 때 고구마 출력하기
            back = Image.open("background.png")
            sweet = Character_sweet((88,70),back) 
            back.paste(sweet.shape,(sweet.position[0], sweet.position[1]))
            joystick.disp.image(back)
            break

        flag, block_out, time = basic.move(back, flag, fireflag, fire, block_out, time, basic_, command)
 
        


if __name__ == '__main__':
    main()