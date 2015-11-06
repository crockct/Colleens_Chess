"""
Colleen Rock's experimentation with pygame
January 2012
"""
from ChessPieces import *
import pygame, sys
import Button

#Global Variables
padding = 10
width = 75
height = 75
wh = (width, height)
BORDER_THICKNESS = 3

DEBUG = True # when True, prints messages to console

rowTopLoc = {"0": padding, "1": height + padding, "2": 160, "3": 235, "4": 310, "5": 385, "6": 460, "7": 535}
colLeftLoc ={"a": padding, "b": width + padding, "c": 160, "d": 235, "e": 310, "f": 385, "g": 460, "h": 535}
colNumber = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

#gives the character, as a string, corresponding to the column num
def colStr(num):
    num = int(num)
    #num = num%8 #deals with negative numbers (poorly)
    if num == 0:
        return 'a'
    elif num == 1:
        return 'b'
    elif num == 2:
        return 'c'
    elif num == 3:
        return 'd'
    elif num == 4:
        return 'e'
    elif num == 5:
        return 'f'
    elif num == 6:
        return 'g'
    elif num == 7:
        return 'h'
    else:
        return 'notASquare'


def get_row_from_mouse_y(y):
    return (y - padding)/height

def get_col_from_mouse_x(x):
    return (x - padding)/width
    

# RGB Color definitions
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red   = (255, 0, 0)
blue  = (0, 0, 255)
yellow= (255, 255, 0)
blue = (50, 100, 255)
green = (50, 175, 75)
    
def newGame():
    if (DEBUG):
        print "Welcome to Chess!"
    
    pygame.init() #initialize all imported pygame modules

    window_size = [1000, 650] # width, height
    screen = pygame.display.set_mode(window_size)

    updateText(screen, "Welcome to Chess!")
    pygame.display.set_caption("Colleen's Chess")

    buttons = pygame.sprite.RenderPlain()
    buttons = Button.makeButton(buttons, screen, "Quit", Button.ButtonType.Quit, white, black)
    Button.makeButton(buttons, screen, "Castle", Button.ButtonType.Castle, green, white)

    board = Board()

    turnCount = 0

    clock = pygame.time.Clock()

    mainLoop(screen, board, turnCount, clock, buttons, False)


#---Text box on right of screen---#
def updateText(screen, message):
    textSize = 20
    font = pygame.font.Font(None, 20)
    textY = 0 + textSize
    text = font.render(message, True, white, black)
    textRect = text.get_rect()
    textRect.centerx = 750
    textRect.centery = textY
    screen.blit(text, textRect)
   

#---Makes Labels for the Squares---#
def labelSquares(screen):
    font = pygame.font.Font(None, 30)
    textY = 630
    text = font.render('a', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = 47.5
    textRect.centery = textY
    screen.blit(text, textRect)

    text = font.render('b', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = 122.5
    textRect.centery = textY
    screen.blit(text, textRect)

    text = font.render('c', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = 197.5
    textRect.centery = textY
    screen.blit(text, textRect)

    text = font.render('d', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = 272.5
    textRect.centery = textY
    screen.blit(text, textRect)

    text = font.render('e', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = 347.5
    textRect.centery = textY
    screen.blit(text, textRect)

    text = font.render('f', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = 422.5
    textRect.centery = textY
    screen.blit(text, textRect)

    text = font.render('g', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = 497.5
    textRect.centery = textY
    screen.blit(text, textRect)

    text = font.render('h', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = 572.5
    textRect.centery = textY
    screen.blit(text, textRect)


    text = font.render('0', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = textY
    textRect.centery = 47.5
    screen.blit(text, textRect)

    text = font.render('1', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = textY
    textRect.centery = 122.5
    screen.blit(text, textRect)

    text = font.render('2', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = textY
    textRect.centery = 197.5
    screen.blit(text, textRect)

    text = font.render('3', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = textY
    textRect.centery = 272.5
    screen.blit(text, textRect)

    text = font.render('4', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = textY
    textRect.centery = 347.5
    screen.blit(text, textRect)

    text = font.render('5', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = textY
    textRect.centery = 422.5
    screen.blit(text, textRect)

    text = font.render('6', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = textY
    textRect.centery = 497.5
    screen.blit(text, textRect)

    text = font.render('7', True, white, black)
    textRect = text.get_rect()
    textRect.centerx = textY
    textRect.centery = 572.5
    screen.blit(text, textRect)

        
# Main program Loop: (called by newGame)
def mainLoop(screen, board, turnCount, clock, buttons, done):
    board.squares.draw(screen) #draw Sprites (Squares)
    if board.border != None:
        pygame.draw.rect(screen, red, board.border, BORDER_THICKNESS)
    board.piecesOnBoard.draw(screen) #draw Sprites (Pieces)
    pygame.display.flip() #update screen
    
    if done == True:
        #Button.makeButton(buttons, screen, "Play Again", Button.ButtonType.PlayAgain, blue, white)
        while done == True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: #user clicks close
                    if (DEBUG):
                        print "Close clicked"
                    done = True
                elif e.type == pygame.MOUSEBUTTONUP:               
                    x, y = e.pos
                    clickedButton = Button.clicked(buttons, e.pos)
                    if (clickedButton != False):
                        if (clickedButton.ButtonType == Button.ButtonType.Quit):
                            clickedButton.kill()
                            makeButton(buttons, screen, "Play Again", Button.ButtonType.PlayAgain, blue, white)
                        elif (clickedButton.ButtonType == Button.ButtonType.PlayAgain):
                            newGame()
                        else:
                            print "no button type"
        #again = raw_input("Would you like to play again? If yes, type 'yes'\n")
        #if again == 'yes':
        #    newGame()
    while done == False:
        currentMouseOverSquare = board.mouseOverSquare
        currentLoc = None
        for e in pygame.event.get():
            if e.type == pygame.QUIT: #user clicks close
                if (DEBUG):
                    print "Close clicked"
                done = True
            elif e.type == pygame.MOUSEBUTTONUP:               
                x, y = e.pos
                clickedButton = Button.clicked(buttons, e.pos)
                if (clickedButton != False):
                    if (clickedButton.ButtonType == Button.ButtonType.Quit):
                        clickedButton.kill()
                        castleButton = buttons.sprites()[0]
                        buttons.empty() # takes castle button out of list, but it's still showing
                        pygame.draw.rect(screen, black, castleButton.rect) # draws black over where the castle button used to be
                        Button.makeButton(buttons, screen, "Play Again", Button.ButtonType.PlayAgain, blue, white)
                        updateText(screen, "Do you want to play again?")
                        mainLoop(screen, board, turnCount, clock, buttons, True)
                    elif (clickedButton.ButtonType == Button.ButtonType.PlayAgain):
                        newGame() #sets done=False, emptys buttons (and puts new quit button in)
                    else:
                        print "no button type"
                row = get_row_from_mouse_y(y)
                col = get_col_from_mouse_x(x)
                currentLoc = colStr(col)+str(row)
                if currentLoc in board.squareDic.keys():
                    if board.selectedPiece == None:
                        board.selectedPiece = board.squareDic[currentLoc].piece
                        board.border = board.squareDic[currentLoc].get_rect()
                    elif (board.selectedPiece.row == str(row) and board.selectedPiece.col == colStr(col)):
                        
                        board.border = None
                        board.selectedPiece = None
                    else:
                        oldLocation = board.selectedPiece.row + "," + board.selectedPiece.col
                        newLocation = str(row) + "," + str(colStr(col))
                        if (DEBUG):
                            print oldLocation #new location
                            print newLocation #old location
                        madeMove, exp = makeMove(screen, board, colStr(col), str(row), turnCount, clock)
                        # returns (bool, string explaination )

                        if madeMove:
                            if (DEBUG):
                                print "made move"
                                print exp
                            if turnCount%2==0:
                                turnColor = 'black'
                            else:
                                turnColor = 'white'
                            if 'Game Over' in exp:
                                updateText(screen, exp)

                                buttons.empty() # takes buttons out of list
                                Button.makeButton(buttons, screen, "Play Again", Button.ButtonType.PlayAgain, blue, white)
                                mainLoop(screen, board, turnCount, clock, buttons, True)

                            else:     
                                updateText(screen, turnColor + " moved from " + oldLocation + " to " + newLocation)
                                turnCount +=1
                                board.border = None
                                board.selectedPiece = None
                                for hSquare in board.highlightedSquares:
                                    hSquare.un_highlight() # unhighlight old possible moves
                        else: #error
                            print "exp: " + exp
                            if (DEBUG):
                                print exp
                            updateText(screen, exp)
                
            elif e.type == pygame.MOUSEMOTION:
                x, y = e.pos
                row = get_row_from_mouse_y(y)
                col = get_col_from_mouse_x(x)
                currentLoc = colStr(col)+str(row)

            if currentLoc in board.squareDic.keys():
                    board.mouseOverSquare = board.squareDic[currentLoc]
                    
            if board.mouseOverSquare != currentMouseOverSquare: # hovering over new square
                if board.selectedPiece == None:
                    for hSquare in board.highlightedSquares:
                        hSquare.un_highlight() # unhighlight old possible moves
                    if isinstance(board.mouseOverSquare, Square):
                        board.highlight_legal_moves()
                        # ^ highlight new available moves

        board.squares.draw(screen) #draw Sprites (Squares)

        if board.border != None:
            pygame.draw.rect(screen, red, board.border, BORDER_THICKNESS)
        
        board.piecesOnBoard.draw(screen) #draw Sprites (Pieces)
        
        labelSquares(screen) # displays letters for columns and numbers for rows

        pygame.display.flip() #update screen

        clock.tick(5)

    pygame.quit() #closes things, keeps idle from freezing
    sys.exit()

# requires that board.selectedPiece != None
def makeMove(screen, board, destCol, destRow, turnCount, clock):
    assert(isinstance(board.selectedPiece, Piece))
    gameOver = False
    move = None
    if turnCount%2==0:
        turnColor = 'black'
    else:
        turnColor = 'white'

    piece = board.selectedPiece
    curCol = piece.col
    curRow = piece.row

    if piece == 'castle': #TODO deal with castling elsewhere
        rookPlace = raw_input("Please give the location of the rook you would like to castle with.\n")
        rook = board.squareDic[rookPlace] #surround with try/catch
        x = True
        while(x):
            isRook = isnstance(rook, Rook)
            if not isRook:
                print  "That's not a rook!"
                rook = raw_input("Please give the location of the rook you would like to castle with.\n")
            else:
                x = False
        if board.Castle(turnColor, rook):
            mainLoop(screen, board, turnCount+1, clock, False)
        else: #Castle method will print out error
            makeMove(board, turnCount)

    else:
        if (DEBUG):
            print piece
        if piece.color != turnColor:
            return False, "You can't move a piece that isn't your color!"
        else:
            try:
                int(destRow)
            except ValueError:
                print "---ERROR---\nThe destination row is not an integer. It is: " + destRow
                return False, "---ERROR---\nThe destination row is not an integer."
            else: # if no exception
                validMove = piece.validMove(board, piece.col, piece.row, destCol, destRow)
                if not validMove[0]:
                    if (DEBUG):
                        print "reason not valid: " + validMove[1]
                    return False, validMove[1] # validMove[1] gives detailed piece specific reason why it can't move that way
                else: #valid move
                    if board.isOccupied(destCol, destRow):
                        if board.squareDic[destCol+destRow].piece.color == turnColor:
                            print "You can't capture your own piece!"
                            # not necessary now that validMove checks to see if its occupied with a piece of the same color
                        else:
                            c = board.capture(piece, destCol, destRow)
                            if isinstance(c, str): # returns a game over message as a string if king is captured
                                if 'Game Over' in c:
                                    gameOver = True
                                if (DEBUG):
                                    print c # prints game over message
                                return True, c # mainLoop(screen, board, turnCount+1, clock, gameOver)
                            elif c: # a piece that was not the king was captured
                                # capture method removes capturer from its previous location
                                return True, "piece captured" # mainLoop(screen, board, turnCount+1, clock, gameOver) #next turn
                    else: # destination not occupied
                        board.squareDic[piece.col+piece.row].piece = None   #removes the piece from its previous location
                        piece.moveTo(board, destCol, destRow)               #puts piece at new location
                    whiteKing, blackKing = board.kingsInCheck()         #are any of the kings in check?
                    gameOverBlack = False
                    gameOverWhite = False
                    checkStatus = ""
                    if whiteKing:
                        checkStatus = "Check on white king"
                        gameOverBlack = board.checkMate(board.whiteKing)
                        if gameOverBlack:
                            checkStatus = "Black wins!"
                    if blackKing:
                        checkStatus = "Check on black king"
                        gameOverWhite = board.checkMate(board.blackKing)
                        if gameOverWhite:
                            checkStatus = "White wins!"
                    return True, checkStatus # mainLoop(screen, board, turnCount+1, clock, gameOverBlack or gameOverWhite)
    

class Square(pygame.sprite.Sprite):
    def __init__(self, row, col, color):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect() #gets a rect object with width and height specified above
        self.rect.x = colLeftLoc[col]
        self.rect.y = rowTopLoc[row]
        self.color = color
        self.piece = None

    def get_rect(self):
        return self.rect

    def highlight(self, color=yellow):
        self.image.fill(color)

    def un_highlight(self):
        self.image.fill(self.color)       

      
class Board:
    def __init__(self):

        self.border = None
        self.highlightedSquares = []
        self.mouseOverSquare = None

        self.selectedPiece = None
        
        #---Initializes Squares (the "Board")---#
        self.squares = pygame.sprite.RenderPlain()
        self.squareDic = {} # square dic keeps track of pieces. Yeah, bad name choice there. 
        for keyR in rowTopLoc.keys():
            for keyC in colLeftLoc.keys():
                if (keyC == 'a' or keyC == 'c' or keyC == 'e' or keyC == 'g'):
                    if int(keyR)%2 == 0:
                        s = Square(keyR, keyC, white)
                    else:
                        s = Square(keyR, keyC, black)
                elif int(keyR)%2 == 0:
                    s = Square(keyR, keyC, black)
                else:
                    s = Square(keyR, keyC, white)
                self.squares.add(s) # sprite group
                self.squareDic[keyC+keyR] = s # dict to keep track of squares. Squares keep track of pieces
        
                   
        #---Initializes All the Pieces---#
        r1, r2 = Rook('white', self, 'a', '0'), Rook('white', self, 'h', '0')
        self.whiteRooks = [r1, r2]
        k1, k2 = Knight('white', self, 'b', '0'), Knight('white', self, 'g', '0')
        self.whiteKnights = [k1, k2]
        b1, b2 = Bishop('white', self, 'c', '0'), Bishop('white', self, 'f', '0')
        self.whiteBishops = [b1, b2]
        self.whiteKing = King('white', self, 'd', '0')
        self.whiteQueen = Queen('white', self, 'e', '0')
        self.whitePawns = [Pawn('white', self, 'a'), Pawn('white', self, 'b'), Pawn('white', self, 'c'), Pawn('white', self, 'd'), \
                          Pawn('white', self, 'e'), Pawn('white', self, 'f'), Pawn('white', self, 'g'), Pawn('white', self, 'h')]
        self.blackPawns = [Pawn('black', self, 'a'), Pawn('black', self, 'b'), Pawn('black', self, 'c'), Pawn('black', self, 'd'), \
                           Pawn('black', self, 'e'), Pawn('black', self, 'f'), Pawn('black', self, 'g'), Pawn('black', self, 'h')]

        r3, r4 = Rook('black', self, 'a', '7'), Rook('black', self, 'h', '7')
        self.blackRooks = [r3, r4]
        k3, k4 = Knight('black', self, 'b', '7'), Knight('black', self, 'g', '7')
        self.blackKnights = [k3, k4]
        b3, b4 = Bishop('black', self, 'c', '7'), Bishop('black', self, 'f', '7')
        self.blackBishops = [b3, b4]
        self.blackKing = King('black', self, 'e', '7')
        self.blackQueen = Queen('black', self, 'd', '7')
      
                          
        #---Adds Pieces to the piecesOnBoard Sprite List---#
        self.piecesOnBoard = pygame.sprite.RenderPlain()
        #White Pieces:
        self.piecesOnBoard.add(r1)
        self.piecesOnBoard.add(r2)
        self.piecesOnBoard.add(k1)
        self.piecesOnBoard.add(k2)
        self.piecesOnBoard.add(b1)
        self.piecesOnBoard.add(b2)
        self.piecesOnBoard.add(self.whiteQueen)
        self.piecesOnBoard.add(self.whiteKing)
        for piece in self.whitePawns:
            self.piecesOnBoard.add(piece)
        #Black Pieces:
        self.piecesOnBoard.add(r3)
        self.piecesOnBoard.add(r4)
        self.piecesOnBoard.add(k3)
        self.piecesOnBoard.add(k4)
        self.piecesOnBoard.add(b3)
        self.piecesOnBoard.add(b4)
        self.piecesOnBoard.add(self.blackQueen)
        self.piecesOnBoard.add(self.blackKing)
        for piece in self.blackPawns:
            self.piecesOnBoard.add(piece)

        self.whitePieces = []
        self.blackPieces = []
        for p in self.piecesOnBoard:
            if p.color == 'black':
                self.blackPieces.append(p)
            elif p.color == 'white':
                self.whitePieces.append(p)
        
            
        self.piecesOffBoard = []

        
    def highlight_legal_moves(self):
        if self.mouseOverSquare != None and self.mouseOverSquare.piece != None:
            currentCol = self.mouseOverSquare.col
            currentRow = self.mouseOverSquare.row
            moves = []
            for col in colLeftLoc.keys():
                for row in rowTopLoc.keys():
                    isValidMove = self.mouseOverSquare.piece.validMove(self, currentCol, currentRow, col, row)
                    if isValidMove == None:
                        print "THIS SHOULD NOT BE RETURNING NONE! " + str(self.selectedPiece) + " " + col + row + " " + str(isValidMove)
                    elif isValidMove[0]:# validMove (boolean, string)
                        moves.append(col+str(row))
            for m in moves:
                theSquare = self.squareDic[m]
                self.highlightedSquares.append(theSquare)
                theSquare.highlight()

        
    ### Method for determining if a King of a certain color can castle with a certain rook
      # The king and rook must have not been moved the entire game
      # The king must not be in check
      # The spaces between the king and rook must be empty
    def castle(self, color, rook):
        if rook.hasMoved == False:
            if color == 'white':
                if self.whiteKing.hasMoved == False and not self.kingInCheck(self.whiteKing):
                    if rook.col == 'a': #closer to king
                        if not isOccupied(self, 'b', '0') and not isOccupied(self, 'c', '0'):
                            rook.moveTo(self, 'c', '0')
                            self.whiteKing.moveTo(self, 'b', '0')
                            self.squareDic["a0"] = None
                            self.squareDic["d0"] = None         
                            return True
                        else:
                            return False
                    else: #rook.col == 'h'
                        if not isOccupied(self, 'e', '0') and not isOccupied(self, 'f', '0') and not isOccupied(self, 'g', '0'):
                            rook.moveTo(self, 'e', '0')
                            self.whiteKing.moveTo(self, 'f', '0')
                            self.squareDic["h0"] = None
                            self.squareDic["d0"] = None
                            return True
                        else:
                            return False
                else:
                    print "Cannot castle. King has been moved or is in check."
                    return False
            elif color == 'black':
                if self.whiteKing.hasMoved == False and not self.kingInCheck(self.blackKing):
                    if rook.col == 'a': #farther from king
                        if not isOccupied(self, 'b', '7') and not isOccupied(self, 'c', '7') and not isOccupied(self, 'd', '7'):
                            rook.moveTo(self, 'd', '7')
                            self.blackKing.moveTo(self, 'c', '7')
                            self.squareDic["a7"] = None
                            self.squareDic["e7"] = None
                            return True
                        else:
                            return False
                    else: #rook.col == 'h'
                        if not isOccupied(self, 'f', '7') and not isOccupied(self, 'g', '7'):
                            rook.moveTo(self, 'f', '7')
                            self.blackKing.moveTo(self, 'g', '7')
                            self.squareDic["h7"] = None
                            self.squareDic["e7"] = None
                            return True
                        else:
                            return False
                else:
                    print "Cannot castle. King has been moved or is in check."
                    return False
        else:
            print "Cannot castle with this rook, this rook has moved."
            return False
                      

    def isOccupied(self, col, row): # a, 0 is top left side corner. "row" is y-value
        return isinstance(self.squareDic[str(col)+str(row)].piece, Piece)

    def capture(self, capturer, col, row):
        assert self.isOccupied(col, row), "Error, nothing to capture!"
        deadPiece = self.squareDic[col+row].piece
        if deadPiece.color == capturer.color:
            return "---ERROR--- Cannot capture your own piece!\n"
        self.piecesOffBoard.append(deadPiece)
        deadPiece.onBoard = False
        self.squareDic[col+row].piece = None # remove dead piece from model of board
        self.piecesOnBoard.remove(deadPiece) # remove dead piece form on board sprite list
        self.squareDic[capturer.col + capturer.row].piece = None # remove capturer from current location. moveTo adds it to its new location
        capturer.moveTo(self, col, row) #self is the board
        if isinstance(deadPiece, King):
            return "Game Over! "+deadPiece.color+" has been defeated."
        else:
            return True
            
    def kingsInCheck(self):
        blackKing = False
        whiteKing = False

        wkCol = self.whiteKing.col
        wkRow = self.whiteKing.row
        bkCol = self.blackKing.col
        bkRow = self.blackKing.row

        for p in self.whitePieces:
            if p.onBoard:
                canMove, string_exp = p.validMove(self, p.col, p.row, bkCol, bkRow)
                if canMove:
                    blackKing = True #black King is in check

        for p in self.blackPieces:
            if p.onBoard:
                canMove, string_exp = p.validMove(self, p.col, p.row, wkCol, wkRow)
                if canMove:
                    whiteKing = True      
        return (whiteKing, blackKing)        
                
    def checkMate(self, king):
        col = int(colNumber[king.col])
        row = int(king.row)
        kingMoves = [(col, row-1), (col, row+1), (col+1, row+1), (col+1, row-1), (col-1, row+1), (col-1, row-1), (col-1, row), (col+1, row)]
        kingLegitMoves = {}
        for s in kingMoves:
            c, r = s
            c = colStr(c)
            r = str(r)
            validMove = king.validMove(self, king.col, king.row, c, r)
            if validMove[0]: #if the king can move here. validmove is boolean, str
                try:
                    if self.squareDic[c+r] == None or (not king.color == self.squareDic[c+r].color): #can't move on to your own piece
                        #can move on empty spaces and spaces with other person's piece
                        kingLegitMoves[(c,r)]=False # add this location to the dictionary
                except(KeyError):
                    print "===== Key Error ====="
                    print "C: " + str(c)
                    print "R: " + str(r)
                    print "c+r: " + str(c+r)
                    print self.squareDic
            # if a piece can capture the king in this location, we will set its value to True
        
        if king.color == 'black':
            for key in kingLegitMoves.keys():
                c, r = key
                for p in self.whitePieces:
                    if p.onBoard:
                        validMove = p.validMove(self, p.col, p.row, c, r)
                        if validMove and not isinstance(validMove, str): #if the piece can move here. (ValidMove returns a string if false)
                            kingLegitMoves[key] = True
            
        elif king.color == 'white':
            for key in kingLegitMoves.keys():
                c, r = key
                for p in self.whitePieces:
                    if p.onBoard:
                        validMove = p.validMove(self, p.col, p.row, c, r)
                        if validMove and not isinstance(validMove, str): #if the piece can move here. (ValidMove returns a string if false)
                            kingLegitMoves[key] = True
        else:
            print "Color Error!"
        if False in kingLegitMoves.values():
            return False
        else:
            return True
 
        

    def promote(self, Pawn):
        Pawn.color
        piece = raw_input("What piece would you like to promote your pawn to?\n")
        #drop down menu?
        pass
    def CaptureInPassing(self):
        pass

#Call new game when this file is run
newGame()

"""
Chess Piece Pics from: http://alltheworldsagame.wordpress.com/2011/05/14/assorted-chess-tools/
"""
