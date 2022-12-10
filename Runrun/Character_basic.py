from PIL import Image, ImageDraw
from Character_slide import Character_slide
from Character_angry import Character_angry
from Character_back import Character_back
from Joystick import Joystick

class Character_basic:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+65, position[1]+65))
        self.shape = Image.open("basic.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.position = position
        self.rectangle = ((position[0], position[1], position[0]+65, position[1]+65))
        self.joystick = Joystick()

    def move(self, back, command = None):
        shadow = ImageDraw.Draw(back)
        self.list = list(self.position)
        if command['move'] == False:
            self.state = None
        else:
            self.state = 'move'

            if command['up_pressed']:
                # if Character_back.flag == 1:
                    if self.list[1] < 179:
                        t = 0
                        while t < 10:
                            
                            shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                            self.list[1] -= 7
                            self.position = tuple(self.list)
                            ori = Character_back((self.list[0],self.list[1]),back) #basic 114 / slide 130 / 
                            back.paste(ori.shape,(ori.position[0], ori.position[1]))
                            self.joystick.disp.image(back)
                            t += 1
                        while t > 0:

                            shadow.rectangle((self.list[0], self.list[1], self.list[0]+65, self.list[1]+65), fill = (255,255,255,100))
                            self.list[1] += 7
                            self.position = tuple(self.list)
                            ori = Character_back((self.list[0],self.list[1]),back) #basic 114 / slide 130 / 
                            back.paste(ori.shape,(ori.position[0], ori.position[1]))
                            self.joystick.disp.image(back)
                            t -= 1
                # elif Character_angry.flag == 1:
                #     back = Image.open("background.png")
                #     angry = Character_angry((self.list[0],114),back) #basic 114 / slide 130 / 
                #     back.paste(angry.shape,(angry.position[0], angry.position[1]))
                #     self.joystick.disp.image(back)
                # elif Character_slide.flag == 1:
                #     back = Image.open("background.png")
                #     slide = Character_slide((self.list[0],130),back) #basic 114 / slide 130 / 
                #     back.paste(slide.shape,(slide.position[0], slide.position[1]))
                #     self.joystick.disp.image(back)

            if command['down_pressed']:
                
                slide = Character_slide((self.list[0],130),back) #basic 114 / slide 130 / 
                back.paste(slide.shape,(slide.position[0], slide.position[1]))
                self.joystick.disp.image(back)
                

            if command['btn_B']:
                
                ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                back.paste(ori.shape,(ori.position[0], ori.position[1]))
                self.joystick.disp.image(back)
                


            if command['btn_A']:
                
                angry = Character_angry((self.list[0],114),back) #basic 114 / slide 130 / 
                back.paste(angry.shape,(angry.position[0], angry.position[1]))
                self.joystick.disp.image(back)
                

            if command['right_pressed']:
                if self.list[0] == 200:
                   
                    ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                    back.paste(ori.shape,(ori.position[0], ori.position[1]))
                    self.joystick.disp.image(back)
                else:
                    self.list[0] += 5
                    self.position = tuple(self.list)
                    
                    ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                    back.paste(ori.shape,(ori.position[0], ori.position[1]))
                    self.joystick.disp.image(back)

            if command['left_pressed']:
                if self.list[0] == -35:
                    
                    ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                    back.paste(ori.shape,(ori.position[0], ori.position[1]))
                    self.joystick.disp.image(back)
                else:
                    self.list[0] -= 5
                    self.position = tuple(self.list)
                    
                    ori = Character_back((self.list[0],114),back) #basic 114 / slide 130 / 
                    back.paste(ori.shape,(ori.position[0], ori.position[1]))
                    self.joystick.disp.image(back)
        return back          
                    