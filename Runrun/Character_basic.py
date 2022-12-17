from PIL import Image, ImageDraw
from Character_slide import Character_slide
from Character_angry import Character_angry
from Character_back import Character_back
from Joystick import Joystick
from time import time


class Character_basic:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+65, position[1]+65))
        self.shape = Image.open("basic.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.position = position
        self.rectangle = ((position[0], position[1], position[0]+65, position[1]+65))
        self.time_ = 0
        self.joystick = Joystick()
        self.count = 0

    def move(self, back, flag, fireflag, fire, fireout, firetime, ch, command = None):
        shadow = ImageDraw.Draw(back)# 메인에서 출력한 화면을 가져온다.
        self.list = list(self.position)
        ori = Character_back((self.list[0],self.list[1]),back)
        slide = Character_slide((self.list[0],130),back)
        gameover = Image.open("gameover.png")
        if command['move'] == False:
            self.state = None
        else:
            self.state = 'move'

            if command['up_pressed']: # 조이스틱을 위로 움직이면 점프를 하게 한다.
                if flag == 0 or flag == 2:
                    if self.list[1] < 179:
                        flag = 0
                        t = 0
                        while t < 11:
                            
                            shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+64), fill = (255,255,255,100))
                            self.list[1] -= 10
                            self.position = tuple(self.list)
                            ori = Character_back((self.list[0],self.list[1]),back) #basic 114 / slide 130 / 
                            back.paste(ori.shape,(ori.position[0], ori.position[1]))
                            self.joystick.disp.image(back)
                            t += 1
                            if fireout == 1:
                                if fireflag == 1:
                                    shadow.rectangle((fire.position[0], fire.position[1]+10, fire.position[0]+30, fire.position[1]+60), fill = (255,255,255,100))
                                    fire.list = list(fire.position)
                                    fire.list[0] -= 10
                                    if fire.list[0] < -60:
                                        fireout =0
                                        firetime -= 1
                                    fire.position = tuple(fire.list)
                                    back.paste(fire.shape,(fire.position[0], fire.position[1]))
                                    self.joystick.disp.image(back)
                                    overlap = (ori.position[0]+65 > fire.position[0]+5 > ori.position[0]) and (ori.position[1]+65 > fire.position[1] + 10)
                                    print(overlap)
                                    if overlap == True:
                                        self.joystick.disp.image(gameover)
                                        exit(0)
                                    firout = 1
                                elif fireflag == 2:
                                    shadow.rectangle((fire.position[0], fire.position[1], fire.position[0]+60, fire.position[1]+60), fill = (255,255,255,100))
                                    fire.list = list(fire.position)
                                    fire.list[0] -= 10
                                    if fire.list[0] < -60:
                                        fireout =0
                                        firetime -= 1
                                    fire.position = tuple(fire.list)
                                    back.paste(fire.shape,(fire.position[0], fire.position[1]))
                                    self.joystick.disp.image(back)
                                    overlap = (ori.position[0]+65 > fire.position[0]+15 > ori.position[0]) and (fire.position[1]+65 > ori.position[1] + 65 >fire.position[1])
                                    print(overlap)
                                    if overlap == True:
                                        self.joystick.disp.image(gameover)
                                        exit(0)
                                    firout = 1
                        while t > 0:

                            shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+64), fill = (255,255,255,100))
                            self.list[1] += 10
                            self.position = tuple(self.list)
                            ori = Character_back((self.list[0],self.list[1]),back) #basic 114 / slide 130 / 
                            back.paste(ori.shape,(ori.position[0], ori.position[1]))
                            self.joystick.disp.image(back)
                            t -= 1
                            if fireout == 1:
                                if fireflag == 1:
                                    shadow.rectangle((fire.position[0], fire.position[1]+10, fire.position[0]+30, fire.position[1]+60), fill = (255,255,255,100))
                                    fire.list = list(fire.position)
                                    fire.list[0] -= 5
                                    if fire.list[0] < -60:
                                        fireout =0
                                    fire.position = tuple(fire.list)
                                    back.paste(fire.shape,(fire.position[0], fire.position[1]))
                                    self.joystick.disp.image(back)
                                    firout = 1
                                    overlap = (ori.position[0]+65 > fire.position[0]+5 > ori.position[0]) and (ori.position[1]+65 > fire.position[1] + 10)
                                    print(overlap)
                                    if overlap == True:
                                        self.joystick.disp.image(gameover)
                                        exit(0)
                                elif fireflag == 2:
                                    shadow.rectangle((fire.position[0], fire.position[1], fire.position[0]+60, fire.position[1]+60), fill = (255,255,255,100))
                                    fire.list = list(fire.position)
                                    fire.list[0] -= 5
                                    if fire.list[0] < -60:
                                        fireout =0
                                    fire.position = tuple(fire.list)
                                    back.paste(fire.shape,(fire.position[0], fire.position[1]))
                                    self.joystick.disp.image(back)
                                    overlap = (ori.position[0]+65 > fire.position[0]+15 > ori.position[0]) and (fire.position[1]+65 > ori.position[1] + 65 >fire.position[1])
                                    print(overlap)
                                    if overlap == True:
                                        self.joystick.disp.image(gameover)
                                        exit(0)
                                    firout = 1

            if command['down_pressed']: # 조이스틱은 밑으로 움직이면 슬라이딩하게 한다
                if flag == 0:
                    shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                    slide = Character_slide((self.list[0],130),back) #basic 114 / slide 130 / 
                    back.paste(slide.shape,(slide.position[0], slide.position[1]))
                    self.joystick.disp.image(back)
                    flag = 2
                    
                

            if command['btn_B']: # B버튼을 누르면 원래 기본 감자로 돌아온다
                if flag == 2:
                    shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                    ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                    back.paste(ori.shape,(ori.position[0], ori.position[1]))
                    self.joystick.disp.image(back)
                    flag = 0
                    


            if command['btn_A']: # A버튼을 누르면 화난 감자로 변한다
                if ch.count < 4:
                    flag = 1
                    shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                    angry = Character_angry((self.list[0],114),back) #basic 114 / slide 130 / 
                    back.paste(angry.shape,(angry.position[0], angry.position[1]))
                    ch.count += 1
                    ch.time_ = time()
                    self.joystick.disp.image(back)
                    
                    
                

            if command['right_pressed']: # 조이스틱을 오른쪽으로 움직이면 앞으로 움직인다
                if flag == 0:
                    if self.list[0] == 200:
                    
                        shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                        ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                        back.paste(ori.shape,(ori.position[0], ori.position[1]))
                        self.joystick.disp.image(back)
                    else:
                        shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                        self.list[0] += 5
                        self.position = tuple(self.list)
                        
                        ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                        back.paste(ori.shape,(ori.position[0], ori.position[1]))
                        self.joystick.disp.image(back)

                elif flag == 2:
                    if self.list[0] == 200:
                    
                        shadow.rectangle((self.list[0], self.list[1]+25, self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                        slide = Character_slide((self.list[0],130),back) #basic 114 / slide 130 / 
                        back.paste(slide.shape,(slide.position[0], slide.position[1]))
                        self.joystick.disp.image(back)
                    else:
                        shadow.rectangle((self.list[0], self.list[1]+25, self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                        self.list[0] += 5
                        self.position = tuple(self.list)
                        slide = Character_slide((self.list[0],130),back) #basic 114 / slide 130 / 
                        back.paste(slide.shape,(slide.position[0], slide.position[1]))
                        self.joystick.disp.image(back)

            if command['left_pressed']: # 조이스틱을 왼쪽으로 움직이면 뒤로 움직인다
                if flag == 0:
                    if self.list[0] == -35:
                        
                        shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                        ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                        back.paste(ori.shape,(ori.position[0], ori.position[1]))
                        self.joystick.disp.image(back)
                    else:
                        shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                        self.list[0] -= 5
                        self.position = tuple(self.list)
                        
                        ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                        back.paste(ori.shape,(ori.position[0], ori.position[1]))
                        self.joystick.disp.image(back)

                elif flag == 2:
                    if self.list[0] == -35:
                    
                        shadow.rectangle((self.list[0], self.list[1]+25, self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                        slide = Character_slide((self.list[0],130),back) #basic 114 / slide 130 / 
                        back.paste(slide.shape,(slide.position[0], slide.position[1]))
                        self.joystick.disp.image(back)
                    else:
                        shadow.rectangle((self.list[0], self.list[1]+25, self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                        self.list[0] -= 5
                        self.position = tuple(self.list)
                        slide = Character_slide((self.list[0],130),back) #basic 114 / slide 130 / 
                        back.paste(slide.shape,(slide.position[0], slide.position[1]))
                        self.joystick.disp.image(back)
        
        if flag == 0 or flag == 2:
            if fireout == 1:
                if fireflag == 1:
                    shadow.rectangle((fire.position[0], fire.position[1]+10, fire.position[0]+30, fire.position[1]+60), fill = (255,255,255,100))
                    fire.list = list(fire.position)
                    fire.list[0] -= 10
                    if fire.list[0] < -60:
                        fireout =0
                        firetime -= 1
                    fire.position = tuple(fire.list)
                    back.paste(fire.shape,(fire.position[0], fire.position[1]))
                    self.joystick.disp.image(back)
                    firout = 1
                elif fireflag == 2:
                    shadow.rectangle((fire.position[0], fire.position[1], fire.position[0]+60, fire.position[1]+60), fill = (255,255,255,100))
                    fire.list = list(fire.position)
                    fire.list[0] -= 10
                    if fire.list[0] < -60:
                        fireout =0
                        firetime -= 1
                    fire.position = tuple(fire.list)
                    back.paste(fire.shape,(fire.position[0], fire.position[1]))
                    self.joystick.disp.image(back)
                    firout = 1

        if flag == 1:
            end = time() - ch.time_
            if end > 3:
                shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+64), fill = (255,255,255,100))
                ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                back.paste(ori.shape,(ori.position[0], ori.position[1]))
                self.joystick.disp.image(back)
                flag = 0
            else:
                if fireout == 1:
                    if fireflag == 1:
                        shadow.rectangle((fire.position[0], fire.position[1]+10, fire.position[0]+30, fire.position[1]+60), fill = (255,255,255,100))
                        fire.list = list(fire.position)
                        fire.list[0] -= 7
                        if fire.list[0] < -60:
                            fireout =0
                            firetime -= 1
                        fire.position = tuple(fire.list)
                        back.paste(fire.shape,(fire.position[0], fire.position[1]))
                        angry = Character_angry((self.list[0],114),back)
                        back.paste(angry.shape,(angry.position[0], angry.position[1]))
                        self.joystick.disp.image(back)
                        firout = 1
                    elif fireflag == 2:
                        shadow.rectangle((fire.position[0], fire.position[1], fire.position[0]+60, fire.position[1]+60), fill = (255,255,255,100))
                        fire.list = list(fire.position)
                        fire.list[0] -= 7
                        if fire.list[0] < -60:
                            fireout =0
                            firetime -= 1
                        fire.position = tuple(fire.list)
                        back.paste(fire.shape,(fire.position[0], fire.position[1]))
                        angry = Character_angry((self.list[0],114),back)
                        back.paste(angry.shape,(angry.position[0], angry.position[1]))
                        self.joystick.disp.image(back)
                        firout = 1
            
        if fireflag == 1:
            if flag == 0:
                overlap = (ori.position[0]+ 65 > fire.position[0]+2 > ori.position[0] )
                if overlap == True:
                    self.joystick.disp.image(gameover)
                    exit(0)
            if flag == 2:
                overlap = (slide.position[0] + 65 > fire.position[0]+2 > slide.position[0])
                if overlap == True:
                    self.joystick.disp.image(gameover)
                    exit(0)

        if fireflag == 2:
            if flag == 0:
                overlap = (ori.position[0]+ 65 > fire.position[0] +15 > ori.position[0]) and (fire.position[1]+40 > ori.position[1])
                if overlap == True:
                    self.joystick.disp.image(gameover)
                    exit(0)


        return flag, fireout, firetime  