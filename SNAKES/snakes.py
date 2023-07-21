import pygame
import random
import os
pygame.init()
pygame.mixer.init()
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snakes")
pygame.display.update()
bgimg = pygame.image.load("snakes.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height))
bgimg = bgimg.convert_alpha()
bgimg1 = pygame.image.load("snakes1.jpg")
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height))
bgimg1 = bgimg1.convert_alpha()
bgimg2 = pygame.image.load("snakes2.jpg")
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height))
bgimg2 = bgimg2.convert_alpha()
clock=pygame.time.Clock()
fps=80 
font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y]) 
def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
      pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bgimg1,(0,0))
        text_screen("Welcome To The Snakes",black,230,250)
        text_screen("Press Space Bar To Play",black,230,290) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load("Angry Birds Theme Song.mp3")
                    pygame.mixer.music.play()
                    gameloop()    
        pygame.display.update()  
        clock.tick(fps)           
def gameloop():
    snk_list=[]
    snk_length=1  
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    score=0
    snake_size=10
    init_velocity=1.35
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore=f.read()   
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))              
            gameWindow.fill(white)
            gameWindow.blit(bgimg2,(0,0))
            text_screen("Game Over Please Enter To Continue",red,100,200)
            text_screen("HIGHSCORE: "+str(highscore),green,280,240)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()    
        else:    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        init_velocity-=0.35
                    if event.key==pygame.K_a:
                        init_velocity+=0.35
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity 
                        velocity_x=0
                    if event.key==pygame.K_q:
                        score+=10          
            snake_x+=velocity_x
            snake_y+=velocity_y 
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                text_screen("Score "+str(score) + "  Highscore: "+str(highscore),blue,5,5)
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                snk_length+=5
                if score>int(highscore):
                    highscore=score
            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score "+str(score) + "  Highscore: "+str(highscore),blue,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True 
                pygame.mixer.music.load("A SQUIRREL SCREAMING FUNNY.mp3")
                pygame.mixer.music.play()   
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load("A SQUIRREL SCREAMING FUNNY.mp3")
                pygame.mixer.music.play()        
            plot_snake(gameWindow,white,snk_list,snake_size)
        pygame.display.update() 
        clock.tick(fps)   
    pygame.quit()
    quit()
welcome()  