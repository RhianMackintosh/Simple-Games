#pygame pracitse
import pygame
pygame.init()

ScreenWidth = 800
ScreenHeight = 800
font = pygame.font.Font("freesansbold.ttf",50)
StartColour = (163,218,246)
StartColourD = (132,205,242)
LogIn = "Log In"
SignIn = "Sign In"

window = pygame.display.set_mode((ScreenWidth,ScreenHeight))
window.fill((255,255,255))
pygame.display.set_caption("Games")
pygame.display.update()

def button(StartColour,x,y,width,height,text,pos1,pos2):
    pygame.draw.rect(window,(StartColour),(x,y,width,height))
    Button2 = font.render(text,1,(0,0,0))
    window.blit(Button2,(pos1,pos2))

#drawing 'buttons'
button(StartColourD,310,410,200,80,SignIn,320,420)
button(StartColour,300,400,200,80,SignIn,320,420)

#drawing the log in
button(StartColourD,310,510,200,80,LogIn,325,520)
button(StartColour,300,500,200,80,LogIn,325,520)    

def Menu():
    selec = False
    while selec == False:
        pygame.display.update()
        mousex,mousey = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mousex,mousey)
        if mousex >= 300 and mousex <= 500 and mousey >= 400 and mousey <= 480:
            button(StartColourD,300,400,200,80,SignIn,320,420)
            pygame.display.update()


            '''if click[0] == 1:
                print("SI YAY")
                selec = True'''

        elif mousex >= 300 and mousex <= 500 and mousey >= 500 and mousey <= 580:
            button(StartColourD,300,500,200,80,LogIn,325,520)
            pygame.display.update()

            '''if click[0] == 1:
                print("LI yay")
                selec = True'''
        else:
            #drawing 'buttons'
            button(StartColourD,310,410,200,80,SignIn,320,420)
            button(StartColour,300,400,200,80,SignIn,320,420)

            #drawing the log in
            button(StartColourD,310,510,200,80,LogIn,325,520)
            button(StartColour,300,500,200,80,LogIn,325,520)

            pygame.display.update()
            


        
#start screen
#log in
#sign up
#menu
#game menu
#game 1
#game 2
#game 3
#profile

Menu()
run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    #if key[pygame.K_SPACE]:
        #start
