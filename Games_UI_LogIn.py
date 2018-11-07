import pygame
pygame.init()

def LogInUI():
    def button(StartColour,x,y,width,height,text,fontC,pos1,pos2):
        pygame.draw.rect(window,(StartColour),(x,y,width,height))
        Button2 = fontC.render(text,1,(0,0,0))
        window.blit(Button2,(pos1,pos2))

    #------------------------------------------------------------------------------
    white = (255,255,255)
    backGC = (217, 240, 252)
    StartColour = (163,218,246)
    StartColourD = (132,205,242)
    ScreenWidth = 800
    ScreenHeight = 800
    big = pygame.font.Font("freesansbold.ttf",50)
    small = pygame.font.Font("freesansbold.ttf",30)
    window = pygame.display.set_mode((ScreenWidth,ScreenHeight))
    window.fill((backGC))
    pygame.display.update()
    #------------------------------------------------------------------------------

    button(StartColourD,260,200,310,80,"Log In",big,320,210)
    button(StartColour,250,190,310,80,"Log In",big,320,210)    
    
    #username input button
    button(StartColour,160,400,180,40,"Username:",small,170,405)
    button(white,350,400,270,40,"",small,170,405)

    #password input button
    button(StartColour,160,500,180,40,"Password:",small,170,505)
    button(white,350,500,270,40,"",small,170,505)

    pygame.display.update()

    selec = False
    while selec == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                print(event.pos)                                                       #Checks mouse position

        
                   
        
        mousex,mousey = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if mousex >= 350 and mousex <= 620 and mousey >= 400 and mousey <= 460:        #checks if mouse is in username box
            button(StartColourD,140,390,500,60,"",small,170,405)
            button(StartColour,160,400,180,40,"Username:",small,170,405)
            button(white,350,400,270,40,"",small,170,405)
            pygame.display.update()


            if click[0] == 1:
                print("username clicked")
                selec = True
                

        elif mousex >= 350 and mousex <= 620 and mousey >= 500 and mousey <= 540:
            button(StartColourD,140,490,500,60,"",small,170,405)
            button(StartColour,160,500,180,40,"Password:",small,170,505)
            button(white,350,500,270,40,"",small,170,505)
            pygame.display.update()

            if click[0] == 1:
                print("password clicked")
                selec = True

        else:
            button(backGC,140,390,500,60,"",small,170,405)
            button(backGC,140,490,500,60,"",small,170,405)
            #username input button
            button(StartColour,160,400,180,40,"Username:",small,170,405)
            button(white,350,400,270,40,"",small,170,405)

            #password input button
            button(StartColour,160,500,180,40,"Password:",small,170,505)
            button(white,350,500,270,40,"",small,170,505)

            pygame.display.update()
            
                


ScreenWidth = 800
ScreenHeight = 800
window = pygame.display.set_mode((ScreenWidth,ScreenHeight))
window.fill((255,255,255))
pygame.display.set_caption("Games")
pygame.display.update()
LogInUI()
