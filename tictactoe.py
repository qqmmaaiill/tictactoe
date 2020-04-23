# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:16:40 2020

@author: IVAN
"""

#pygame lib for GUI
import pygame
#sys.exit()
import sys
#for time.sleep()
import time

#Who is the winner of the game,starts with no one
winner = None
#For while loop - if it's false ,then the game has finished
running = True
#draw check
draw = False

XO = 'x'

#size of the screen

width = 400
height = 400

#parameters for a white color for an easier use
white =(255,255,255)
#color of the separating lines for the screen 3x3
line_c = (20,20,20)


#board itself
TTT = [[None]*3,[None]*3,[None]*3]


#init the pygame structure
pygame.init()
fps = 60
CLOCK = pygame.time.Clock()
#show a picture(width,height,flag,depth,display=0)
screen = pygame.display.set_mode((width,height+100),0,32)
#caption of the window(name)
pygame.display.set_caption("Tic tac toe")

#load images for the game and X and O

opening = pygame.image.load('tic tac opening.png')
x_img = pygame.image.load('x.png')
o_img = pygame.image.load('o.png')

#resize

x_img = pygame.transform.scale(x_img,(75,75))
o_img = pygame.transform.scale(o_img,(75,75))
opening = pygame.transform.scale(opening,(width,height+100))

#start drawing on window

def game_open():
    
    #what to draw and from what dest(upper left of the screen)
    screen.blit(opening,(0,0))
    
    pygame.display.update()
    
    time.sleep(2)
    
    screen.fill(white)

    #draw vert lines,then horiz lines
    #where to draw,color,start point,end point,thickness(<1 - not drawn)
    pygame.draw.line(screen,line_c,(width/3,0),(width/3,height),7)
    pygame.draw.line(screen,line_c,(width/3*2,0),(width/3*2,height),7)
    
    pygame.draw.line(screen,line_c,(0,height/3),(width,height/3),7)
    pygame.draw.line(screen,line_c,(0,height/3*2),(width,height/3*2),7)
    
    draw_status()

def draw_status():
    
    #using the global variable draw in the function,any changes to draw WILL apply to the global variable draw
    global draw
    
    if winner is None and draw == False:
        mesg = XO.upper() + "'s turn!!!"
    elif draw == True:
        mesg = "Draw!!!"
    else:
        mesg = winner.upper() + ' WON!!!'
        
    #create a Font surface
    font = pygame.font.Font(None,30)
    #text variable to render the text on the screen
    text = font.render(mesg,1,white)
    
    #copy message to screen
    screen.fill((0,0,0),(0,400,500,100))
    text_rect = text.get_rect(center=(width/2,450))
    screen.blit(text,text_rect)
    pygame.display.update()
    
def check_w():
    global TTT
    global winner
    global draw
    #check rows
    for row in range(0,3):
        if((TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None)):
            winner = TTT[row][0]
            #draw line across the winning tiles
            pygame.draw.line(screen,(250,0,0),(0,(2*row +1)*height/6),(width,(2*row+1)*height/6),5)
            break
    #check columns
    for col in range(0,3):
        if((TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None)):
            winner = TTT[0][col]
            pygame.draw.line(screen,(250,0,0),((2*col+1)*width/6,0),((2*col+1)*width/6,height),5)
            break
    #check first diagonal
    if((TTT[0][0]==TTT[1][1]==TTT[2][2]) and (TTT[0][0] is not None)):
        winner = TTT[0][0]
        pygame.draw.line(screen,(250,0,0),(0,0),(width,height),5)
    #check other diagonal
    if((TTT[0][2]==TTT[1][1]==TTT[2][0]) and (TTT[0][2] is not None)):
        winner = TTT[0][2]
        pygame.draw.line(screen,(250,0,0),(0,height),(width,0),5)
    
    if(all([all(row) for row in TTT]) and winner is None):
        draw = True
    
    draw_status()
#draw picture by row and col    
def drawXO(row,col):
    global TTT
    global XO
    
    if row == 1:
        posx = 30
    if row == 2:
        posx = width/3 + 30
    if row == 3:
        posx = width/3*2 + 30
        
    if col == 1:
        posy = 30
    if col == 2:
        posy = height/3 + 30
    if col == 3:
        posy = height/3*2 + 30
    #"draw" in TTT   
    TTT[row-1][col-1] = XO
    #draw on screen
    if XO == 'x':
        screen.blit(x_img,(posy,posx))
        XO = 'o'
    else:
        screen.blit(o_img,(posy,posx))
        XO = 'x'
    
    pygame.display.update()
    
def userC():
    #defined in pygame,returns coordinates of the mouse click as pair
    x,y = pygame.mouse.get_pos()
    
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None
        
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
        
    if(row and col and TTT[row-1][col-1] is None):
        global XO
        
        drawXO(row,col)
        
        check_w()
 
def reset():
    global TTT
    global winner
    global draw
    global XO
    time.sleep(5)
    xo = 'x'
    draw = False
    winner = None
    TTT = [[None]*3,[None]*3,[None]*3]
    game_open()



#run the game
#call the start-game_open    
game_open()

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            userC()
            if(winner or draw):
                reset()
    
    pygame.display.update()
    #CLOCK.tick(fps)
    

    
    