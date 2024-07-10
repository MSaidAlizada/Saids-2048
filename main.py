import pygame
import random
from copy import deepcopy

pygame.init()

#Setting up the window
windowHeight = 700
windowWidth = 700
window = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("2048")

#Helper functions for development
def printMousePosition():
    print(pygame.mouse.get_pos())


#Class for the squares
class Square:
    def __init__(self, number, cords):
        self.number = number
        self.cords = cords
        self.size = 150
        self.color = (205, 193, 181)
    def moveBox(self, direction,boxCords,grid):
        global score
        global highestNum
        moved = False
        if direction == "r":
            if boxCords[0] != 3:
                if grid[boxCords[1]][boxCords[0]+1].number == 0:
                    moved = True
                    grid[boxCords[1]][boxCords[0]+1].number = self.number
                    self.number = 0
                    grid[boxCords[1]][boxCords[0]+1].moveBox("r",[boxCords[0]+1,boxCords[1]], grid)
                if grid[boxCords[1]][boxCords[0]+1].number == self.number:
                    grid[boxCords[1]][boxCords[0]+1].number = 2*self.number
                    score += 2*self.number
                    if 2*self.number > highestNum:
                        highestNum = 2*self.number
                    self.number = 0
        elif direction == "l":
            if boxCords[0] != 0:
                if grid[boxCords[1]][boxCords[0]-1].number == 0:
                    moved = True
                    grid[boxCords[1]][boxCords[0]-1].number = self.number
                    self.number = 0
                    grid[boxCords[1]][boxCords[0]-1].moveBox("l",[boxCords[0]-1,boxCords[1]], grid)
                if grid[boxCords[1]][boxCords[0]-1].number == self.number:
                    grid[boxCords[1]][boxCords[0]-1].number = 2*self.number
                    score += 2*self.number
                    if 2*self.number > highestNum:
                        highestNum = 2*self.number
                    self.number = 0
        elif direction == "u":
            if boxCords[1] != 0:
                if grid[boxCords[1]-1][boxCords[0]].number == 0:
                    moved = True
                    grid[boxCords[1]-1][boxCords[0]].number = self.number
                    self.number = 0
                    grid[boxCords[1]-1][boxCords[0]].moveBox("u",[boxCords[0],boxCords[1]-1], grid)
                if grid[boxCords[1]-1][boxCords[0]].number == self.number:
                    grid[boxCords[1]-1][boxCords[0]].number = 2*self.number
                    score += 2*self.number
                    if 2*self.number > highestNum:
                        highestNum = 2*self.number
                    self.number = 0
        elif direction == "d":
            if boxCords[1] != 3:
                if grid[boxCords[1]+1][boxCords[0]].number == 0:
                    moved = True
                    grid[boxCords[1]+1][boxCords[0]].number = self.number
                    self.number = 0
                    grid[boxCords[1]+1][boxCords[0]].moveBox("d",[boxCords[0],boxCords[1]+1], grid)
                if grid[boxCords[1]+1][boxCords[0]].number == self.number:
                    grid[boxCords[1]+1][boxCords[0]].number = 2*self.number
                    score += 2*self.number
                    if 2*self.number > highestNum:
                        highestNum = 2*self.number
                    self.number = 0
        return moved
    def draw(self):
        match self.number:
            case 0:
                self.color = (205, 193, 181)
            case 2:
                self.color = (238, 228, 218)
                textColor =  (118, 111, 101)
            case 4:
                self.color = (237, 225, 200)
                textColor =  (118, 111, 101)
            case 8:
                self.color = (243, 178, 121)
                textColor = (250, 246, 243)
            case 16:
                self.color = (245, 151, 101)
                textColor = (250, 246, 243)
            case 32:
                self.color = (247, 123, 94)
                textColor = (250, 246, 243)
            case 64:
                self.color = (250, 117, 75)
                textColor = (250, 246, 243)
            case 128:
                self.color = (241, 215, 134)
                textColor = (250, 246, 243)
            case 256:
                self.color = (241, 212, 117)
                textColor = (250, 246, 243)
            case 512:
                self.color = (241, 208, 98)
                textColor = (250, 246, 243)
            case 1024:
                self.color = (241, 206, 79)
                textColor = (250, 246, 243)
            case 2048:
                self.color = (241, 203, 58)
                textColor = (250, 246, 243)
        pygame.draw.rect(window, (188, 172, 159), (self.cords[0]+50, self.cords[1]+80, self.size, self.size))
        pygame.draw.rect(window, self.color, (self.cords[0]+60, self.cords[1]+90, self.size-20, self.size-20))
        if self.number != 0:
            DrawText(str(self.number),60,textColor,(self.cords[0]+50+self.size/2),(self.cords[1]+80+self.size/2))

#Class for buttons
class Button:
    def __init__(self,text,x,y):
        self.text = text
        self.x = x
        self.y = y
        self.xsize = 150
        self.ysize = 50
        self.color = (142, 122, 103)
        self.textColor = (250, 246, 243)
    def clicked(self):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if x>self.x and x<self.x+self.xsize and y>self.y and y<self.y+self.ysize:
            Reset()
    def draw(self):
        pygame.draw.rect(window, self.color, (self.x,self.y,self.xsize,self.ysize))
        DrawText(self.text, 20,self.textColor,(self.x+self.xsize/2),(self.y+self.ysize/2))

#Helper functions for game
def Reset():
    global board
    global moveNum
    global score
    global highestNum
    board = [[Square(0,[0,0]),Square(0,[size,0]),Square(0,[2*size,0]),Square(0,[3*size,0])],
         [Square(0,[0,size]),Square(0,[size,size]),Square(0,[2*size,size]),Square(0,[3*size,size])],
         [Square(0,[0,2*size]),Square(0,[size,2*size]),Square(0,[2*size,2*size]),Square(0,[3*size,2*size])],
         [Square(0,[0,3*size]),Square(0,[size,3*size]),Square(0,[2*size,3*size]),Square(0,[3*size,3*size])]]
    moveNum = 0
    score = 0
    board = AddBoxes(board)
    highestNum = 0

def GetEmptyBoxes(board):
    boxes = []
    for i in board:
        for j in i:
            if j.number == 0:
                boxes.append(j)
    return boxes

def AddBoxes(board):
    global move
    if  random.random() > 0.1:
        number = 2
    else:
        number = 4
    if len(GetEmptyBoxes(board)) > 0:
        random.choice(GetEmptyBoxes(board)).number = number
    return board
    
def move(direction, moveBoard):
    moved = False
    match direction:
        case "r":
            istep = 1
            jstep = -1
            istart = 0
            iend = 4
            jstart = 2
            jend = -1
        case "l":
            istep = 1
            jstep = 1
            istart = 0
            iend = 4
            jstart = 1
            jend = 4
        case "u":
            istep = 1
            jstep = 1
            istart = 1
            iend = 4
            jstart = 0
            jend = 4
        case "d":
            istep = -1
            jstep = 1
            istart = 2
            iend = -1
            jstart = 0
            jend = 4   
    for i in range(istart,iend,istep):
        for j in range(jstart,jend,jstep):
            if moveBoard[i][j].number != 0:
                res = moveBoard[i][j].moveBox(direction, [j,i], moveBoard)
                if res:
                    moved = True
    return moved

def GameOver():
    global board
    if len(GetEmptyBoxes(board)) == 0:
        for i in ["r","l","u","d"]:
            board_copy = deepcopy(board)
            if move(i, board_copy):
                return False
        return True
    return False

def DrawText(text, size, color, x, y):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    window.blit(text, textRect)

def DrawScore():
    global score
    pygame.draw.rect(window, (188, 172, 159), (50,5,150,70))
    DrawText("SCORE", 20, (238, 228, 218), 125,20)
    DrawText(str(score),40,(255,255,255), 125,50)

#main game loop
size = 150
board = [[Square(0,[0,0]),Square(0,[size,0]),Square(0,[2*size,0]),Square(0,[3*size,0])],
         [Square(0,[0,size]),Square(0,[size,size]),Square(0,[2*size,size]),Square(0,[3*size,size])],
         [Square(0,[0,2*size]),Square(0,[size,2*size]),Square(0,[2*size,2*size]),Square(0,[3*size,2*size])],
         [Square(0,[0,3*size]),Square(0,[size,3*size]),Square(0,[2*size,3*size]),Square(0,[3*size,3*size])]]
score = 0
highestNum = 0
running = True
newGameBtn = Button("New Game", 500, 20)
tryAgainBtn = Button("Try again", 275, 400)
restartBtn = Button("Restart", 275, 400)
AddBoxes(board)
while running:
    pygame.time.delay(100)
    window.fill((250, 248, 239))
    #Getting all events
    for event in pygame.event.get():
        #Checking if window gets closed
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            newGameBtn.clicked()
            if GameOver():
                tryAgainBtn.clicked()
            if highestNum == 2048:
                restartBtn.clicked()
    #Getting keyboard input
    pressed = pygame.key.get_pressed()
    if highestNum != 2048:
        if pressed[pygame.K_RIGHT]:
            if move("r",board):
                board = AddBoxes(board)
        if pressed[pygame.K_LEFT]:
            if move("l",board):
                board = AddBoxes(board)
        if pressed[pygame.K_UP]:
            if move("u",board):
                board = AddBoxes(board)
        if pressed[pygame.K_DOWN]:
            if move("d",board):
                board = AddBoxes(board)
        if pressed[pygame.K_r]:
            Reset()
    #Drawing the score
    DrawScore()
    #Drawing new game button
    newGameBtn.draw()
    #Drawing the board
    for i in board:
        for j in i:
            j.draw()
    #Checkif if they won
    if highestNum == 2048:
        pygame.time.delay(50)
        surface = pygame.Surface((600,600), pygame.SRCALPHA)
        surface.fill((213, 183, 101,180))
        window.blit(surface, (50,80))
        DrawText("You win!",50,(246, 247, 237),350,350)
        restartBtn.draw()
    #Checking if game over
    if GameOver():
        pygame.time.delay(50)
        surface = pygame.Surface((600,600), pygame.SRCALPHA)
        surface.fill((238,227,214,200))
        window.blit(surface, (50,80))
        DrawText("Game Over!",50,(118, 111, 101),350,350)
        tryAgainBtn.draw()
    pygame.display.update()

pygame.quit()