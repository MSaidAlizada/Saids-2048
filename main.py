import pygame
import random

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
    def __init__(self, number, move, cords):
        self.number = number
        self.move = move
        self.cords = cords
        self.size = 150
        self.color = (205, 193, 181)
    def moveBox(self, direction,boxCords):
        moved = False
        if direction == "r":
            if boxCords[0] != 3:
                if board[boxCords[1]][boxCords[0]+1].number == 0:
                    moved = True
                    board[boxCords[1]][boxCords[0]+1].number = self.number
                    self.number = 0
                    board[boxCords[1]][boxCords[0]+1].moveBox("r",[boxCords[0]+1,boxCords[1]])
                if board[boxCords[1]][boxCords[0]+1].number == self.number:
                    board[boxCords[1]][boxCords[0]+1].number = 2*self.number
                    self.number = 0
        elif direction == "l":
            if boxCords[0] != 0:
                if board[boxCords[1]][boxCords[0]-1].number == 0:
                    moved = True
                    board[boxCords[1]][boxCords[0]-1].number = self.number
                    self.number = 0
                    board[boxCords[1]][boxCords[0]-1].moveBox("l",[boxCords[0]-1,boxCords[1]])
                if board[boxCords[1]][boxCords[0]-1].number == self.number:
                    board[boxCords[1]][boxCords[0]-1].number = 2*self.number
                    self.number = 0
        elif direction == "u":
            if boxCords[1] != 0:
                if board[boxCords[1]-1][boxCords[0]].number == 0:
                    moved = True
                    board[boxCords[1]-1][boxCords[0]].number = self.number
                    self.number = 0
                    board[boxCords[1]-1][boxCords[0]].moveBox("u",[boxCords[0],boxCords[1]-1])
                if board[boxCords[1]-1][boxCords[0]].number == self.number:
                    board[boxCords[1]-1][boxCords[0]].number = 2*self.number
                    self.number = 0
        elif direction == "d":
            if boxCords[1] != 3:
                if board[boxCords[1]+1][boxCords[0]].number == 0:
                    moved = True
                    board[boxCords[1]+1][boxCords[0]].number = self.number
                    self.number = 0
                    board[boxCords[1]+1][boxCords[0]].moveBox("d",[boxCords[0],boxCords[1]+1])
                if board[boxCords[1]+1][boxCords[0]].number == self.number:
                    board[boxCords[1]+1][boxCords[0]].number = 2*self.number
                    self.number = 0
        return moved
    def draw(self):
        match self.number:
            case 0:
                self.color = (205, 193, 181)
            case 2:
                self.color = (238, 228, 218)
            case 4:
                self.color = (237, 225, 200)
            case 8:
                self.color = (243, 178, 121)
            case 16:
                self.color = (245, 151, 101)
            case 32:
                self.color = (247, 123, 94)
            case 64:
                self.color = (250, 117, 75)
            case 128:
                self.color = (241, 215, 134)
            case 256:
                self.color = (241, 212, 117)
            case 512:
                self.color = (241, 208, 98)
            case 1024:
                self.color = (241, 206, 79)
            case 2048:
                self.color = (241, 203, 58)
        pygame.draw.rect(window, (188, 172, 159), (self.cords[0]+50, self.cords[1]+60, self.size, self.size))
        pygame.draw.rect(window, self.color, (self.cords[0]+60, self.cords[1]+70, self.size-20, self.size-20))

#Helper functions for game
def Reset():
    global board
    global moveNum
    global score
    board = [[Square(0,0,[0,0]),Square(0,0,[size,0]),Square(0,0,[2*size,0]),Square(0,0,[3*size,0])],
         [Square(0,0,[0,size]),Square(0,0,[size,size]),Square(0,0,[2*size,size]),Square(0,0,[3*size,size])],
         [Square(0,0,[0,2*size]),Square(0,0,[size,2*size]),Square(0,0,[2*size,2*size]),Square(0,0,[3*size,2*size])],
         [Square(0,0,[0,3*size]),Square(0,0,[size,3*size]),Square(0,0,[2*size,3*size]),Square(0,0,[3*size,3*size])]]
    moveNum = 0
    score = 0
    board = AddBoxes(board)

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
    
def move(direction):
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
            if board[i][j].number != 0:
                res = board[i][j].moveBox(direction, [j,i])
                if res:
                    moved = True
    return moved


#main game loop
size = 150
board = [[Square(0,0,[0,0]),Square(0,0,[size,0]),Square(0,0,[2*size,0]),Square(0,0,[3*size,0])],
         [Square(0,0,[0,size]),Square(0,0,[size,size]),Square(0,0,[2*size,size]),Square(0,0,[3*size,size])],
         [Square(0,0,[0,2*size]),Square(0,0,[size,2*size]),Square(0,0,[2*size,2*size]),Square(0,0,[3*size,2*size])],
         [Square(0,0,[0,3*size]),Square(0,0,[size,3*size]),Square(0,0,[2*size,3*size]),Square(0,0,[3*size,3*size])]]
moveNum = 0
score = 0
running = True
board = AddBoxes(board)
while running:
    pygame.time.delay(100)
    window.fill((250, 248, 239))
    #Getting all events
    for event in pygame.event.get():
        #Checking if window gets closed
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            printMousePosition()
    #Getting keyboard input
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        if move("r"):
            board = AddBoxes(board)
    if pressed[pygame.K_LEFT]:
        if move("l"):
            board = AddBoxes(board)
    if pressed[pygame.K_UP]:
        if move("u"):
            board = AddBoxes(board)
    if pressed[pygame.K_DOWN]:
        if move("d"):
            board = AddBoxes(board)
    if pressed[pygame.K_r]:
        Reset()
    #Drawing the board
    for i in board:
        for j in i:
            j.draw()
    pygame.display.flip()

pygame.quit()