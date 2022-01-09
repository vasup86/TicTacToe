import pygame
import os
import time

pygame.init()
#Window height and Width
WIDTH, HEIGHT = 300,300
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#Window title
pygame.display.set_caption('Tic Tac Toe')

FPS = 60 #refresh rate for window

BLACK = (0,0,0)
WHITE = (255,255,255)
BACKGROUNDCOLOR = (65,179,163) #greenish

#(0,1,2),(3,4,5),(6,7,8)
IMGLOCATION = [(40,40), (130,40), (220,40), (40,130), (130,130), (220,130), (40,220), (130,220),(220,220)]

#FIX IMAGES for cross and circle
CROSS = pygame.image.load(os.path.join("res" , "cross (2).png"))
CIRCLE = pygame.image.load(os.path.join("res", "circle (2).png"))

#check for tie
roundCount = 1

#Board (row,col) (3*3 2D-array board)
board = [0,0,0,0,0,0,0,0,0]

# 'O' player will be 1, 'X' player will be 2

def endText(win,posX, posY, fontSize):
    FONT = pygame.font.Font('freesansbold.ttf', fontSize)
    text = FONT.render(win, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (posX, posY)
    WIN.blit(text, textRect)

def endWindow(win):
    WIN.fill(BACKGROUNDCOLOR)   
    endText(win, WIDTH//2, (HEIGHT//2)-10, 32)
    pygame.draw.rect(WIN,BLACK,(40,210,100,20)) #play again box
    endText('Play again', 90,220,18)
    pygame.draw.rect(WIN,BLACK,(175,210,50,20)) #Quit box
    endText('Quit', 200,220,18)
    pygame.display.update()

def endSlide(win):
    global roundCount
    global winnerPlayer
    global board
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if close the window, exit the loop
                pygame.quit()
            endWindow(win)
        if((pygame.mouse.get_pressed())[0]):
            checkExit()
            pos = pygame.mouse.get_pos()
            posX = pos[0]
            posY= pos[1]
            if((posX>=40 and posX<=140)and(posY>=210 and posY<=230)):
                roundCount = 1
                winnerPlayer=0
                board = [0,0,0,0,0,0,0,0,0] #reset the board
                time.sleep(0.3) #sleep for 300ms, its to not confuse the system click for play again with turn
                main()
            elif((posX>=175 and posX<=225) and (posY>=210 and posY<=230)):
                pygame.display.quit()

def getSquare(posX, posY):
    if((posX>= 20 and posX<=97) and (posY>=20 and posY<=97)): 
        return 0

    if((posX>= 105 and posX<=195) and (posY>=20 and posY<=97)):
        return 1
    
    if((posX>= 205 and posX<=280) and (posY>=20 and posY<=97)):
        return 2
    
    if((posX>= 20 and posX<=97) and (posY>=105 and posY<=196)):
        return 3
    
    if((posX>= 105 and posX<=195) and (posY>=105 and posY<=196)):
        return 4
    
    if((posX>= 205 and posX<=280) and (posY>=105 and posY<=196)):
        return 5
    
    if((posX>= 20 and posX<=97) and (posY>=205 and posY<=280)):
        return 6
    
    if((posX>= 105 and posX<=195) and (posY>=205 and posY<=280)):
        return 7
    
    if((posX>= 205 and posX<=280) and (posY>=205 and posY<=280)):
        return 8
    
def checkBoard():
    global winnerPlayer
    for i in range (1,3): #check for player 1 and 2 using loop
        if(board[0] == i and board[1] == i and board[2] == i): #top horizontal
            winnerPlayer= i
            return False
        if(board[3] == i and board[4] == i and board[5] == i): #middle horizontal
            winnerPlayer = i
            return False
        if(board[6] == i and board[7] == i and board[8] == i): #bottom horizontal
            winnerPlayer = i
            return False
        if(board[0] == i and board[3] == i and board[6] == i): #right vertical
            winnerPlayer = i
            return False
        if(board[1] == i and board[4] == i and board[7] == i): #middle vertical
            winnerPlayer = i
            return False
        if(board[2] == i and board[5] == i and board[8] == i): #left vertical
            winnerPlayer = i
            return False
        if(board[0] == i and board[4] == i and board[8] == i): #backslash
            winnerPlayer = i
            return False
        if(board[2] == i and board[4] == i and board[6] == i): #forward slash
            winnerPlayer = i
            return False
    return True

def round(player):
    global roundCount
    pos = pygame.mouse.get_pos() #get player position (tuple)
    posX = pos[0]
    posY = pos[1]
    square = getSquare(posX, posY)
    if square is None: #if clicked on line or outside box
        return None

    if board[square]==1 or board[square]==2: # if click on taken square
        return None

    if player == 1:  #player 'O'
        #blit(icon, position)
        #WIN.blit(CROSS, IMGLOCATION[0])
        WIN.blit(CIRCLE, IMGLOCATION[square])
        board[square] = 1
        pygame.display.update()
        roundCount+=1
    else: #player 'X'
        WIN.blit(CROSS, IMGLOCATION[square])
        board[square] = 2
        pygame.display.update()
        roundCount+=1
    print(board)
    return (checkBoard()) #change it later

def drawWindow():
    WIN.fill(BACKGROUNDCOLOR) #Background color: RGB

    #blit, text or img to put on screen
    
    #line(window, color, start pos, end pos, width(optional))
    pygame.draw.line(WIN, WHITE, (20,100), (280,100),8)
    pygame.draw.line(WIN, WHITE, (20,200), (280,200),8)
    pygame.draw.line(WIN, WHITE, (100,20), (100,280),8)
    pygame.draw.line(WIN, WHITE, (200,20), (200,280),8)

    pygame.display.update() #update the display

def checkExit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if close the window, exit the loop
            pygame.quit()  #close the window

def main():
    winner = True
    clock = pygame.time.Clock()
    drawWindow()
    playerToggle=1
    while winner or (winner is None):   #none is due to FPS speed 
        clock.tick(FPS) #Run the while loop FPS amount of time.
        checkExit()
        if ((pygame.mouse.get_pressed())[0]): #checks if clicked, first index will be true
            checkExit()
            if(playerToggle%2 != 0): #odd will be player 1, ('O')
                winner = round(1)
            else: #even will be player 2, ('X')
                winner = round(2)
            
            if winner is None: #if click the line or outside the box, it does not count
                continue
            else:
                playerToggle +=1

        if(roundCount==10):
            break
    
    time.sleep(0.25)
    if(winnerPlayer == 1):
        endSlide('Winner is Player 1')
    elif(winnerPlayer == 2):
        endSlide('Winner is Player 2')
    elif (roundCount == 10):
        endSlide('tie')

    time.sleep(30)
    pygame.quit()  #close the window

if __name__ == "__main__":  
    roundCount=1
    winnerPlayer=0
    main()