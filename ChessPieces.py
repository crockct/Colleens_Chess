from pygame import sprite, image

colNumber = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

#gives the character, as a string, corresponding to the column num
def colStr(num):
    num = int(num)
    num = num%8 #deals with negative numbers
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
    else:
        return 'h'

class Piece(sprite.Sprite):
    def __init__(self, color, board, col, row):
        sprite.Sprite.__init__(self)
        self.color = color
        self.col = col
        self.row = row
        self.rect = board.squareDic[self.col+self.row].get_rect()
        self.rect.centerx = board.squareDic[self.col+self.row].get_rect().centerx
        self.rect.centery = board.squareDic[self.col+self.row].get_rect().centery

        self.onBoard = True
        board.squareDic[str(col)+str(row)].piece = self
        self.hasMoved = False #used for Castling

        self.setPic()

    # Requires Capture or not isOccupied
    def moveTo(self, board, col, row):
        board.squareDic[str(col)+str(row)].piece = self
        self.col = col
        self.row = row
        self.hasMoved = True
        self.rect = board.squareDic[self.col+self.row].get_rect()
    
class Rook(Piece): #Rook is a subclass of piece and inherits its attributes and methods
    def setPic(self):
        if (self.color == 'black'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\BlackRook.png").convert_alpha()
            # convert alpha preserves per pixel transparency
        elif (self.color == 'white'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\whiteRook.png").convert_alpha()
        else:
            print "Color issue with Rook"

    def __str__(self):
        return self.color + " rook"
    
    #returns True or String error message
            #requires that currentRow and destRow are numbers
    def validMove(self, board, currentCol, currentRow, destCol, destRow): #row is y value
        #input is string values below values (X Y) are numerical ints
        if board.isOccupied(destCol, destRow) and board.squareDic[destCol + destRow].piece.color == self.color:
                return False, "Can't capture your own piece"
        currentX = colNumber[currentCol]
        currentY = int(currentRow)
        destX = colNumber[destCol]
        destY = int(destRow)

        if (currentX == destX and currentY == destY): #doesn't actually move
            return (False, "same dest and current loc")
        elif destX > 7 or destX < 0 or destY > 7 or destX < 0: #goes off grid
            return (False, "off grid")
        elif currentX == destX:
            if abs(currentY - destY) == 1: #no spaces in between
                return (True, "")
            elif currentY < destY:
                tempY = currentY + 1
                while tempY < destY:
                    if board.isOccupied(destCol, str(tempY)): # col, row
                        return (False, "Rook cannot leap over other pieces")
                    tempY +=1
                return (True, "")
            else: #currentY > destY, need to decrement tempY
                tempY = currentY - 1
                while tempY > destY:
                    if board.isOccupied(destCol, tempY): # col, row
                        return (False, "Rook cannot leap over other pieces.")
                    tempY -=1
                return (True, "")              
        elif currentY == destY:
            numToCheck = abs(currentY - destY) #actually numtoCheck +1
            if numToCheck == 1:
                return (True, "") #no spaces in between
            sList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            i = 0
            s = sList[i]
            while currentCol != s and destCol != s:
                i+=1
                s = sList[i]
            j = 1
            while j < numToCheck:
                if board.isOccupied(sList[i+j], destY):
                    return (False, "This piece cannot leap over other pieces.")
                j+=1
            return (True, "")
        else:
            return (False, "not valid rook move")

class Knight(Piece):
    def setPic(self):
        if (self.color == 'black'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\BlackKnight.png").convert_alpha()
            # convert alpha preserves per pixel transparency
        elif (self.color == 'white'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\whiteKnight.png").convert_alpha()
        else:
            print "Color issue with Knight"

    def __str__(self):
        return self.color + " knight"
    
    #reutrns True or a string error message
    def validMove(self, board, currentCol, currentRow, destCol, destRow): #row is y value
        #input is string values below values (X Y) are numerical ints
        if board.isOccupied(destCol, destRow) and board.squareDic[destCol + destRow].piece.color == self.color:
                return False, "Can't capture your own piece"
        currentX = colNumber[currentCol]
        currentY = int(currentRow)
        destX = colNumber[destCol]
        destY = int(destRow)
        if (currentX == destX and currentY == destY): #doesn't actually move
            return False, "That's not moving1"
        elif destX > 7 or destX < 0 or destY > 7 or destX < 0: #goes off grid
            return False, "You cannot move your piece off the grid"
        else:
            absX = abs(destX-currentX)
            absY = abs(destY-currentY)
            if absY == 2 and absX == 1 or absY ==1 and absX == 2:
                return True, ""
            else:
                return False, "Knights cannot move in this way"

class Bishop(Piece):
    def setPic(self):
        if (self.color == 'black'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\BlackBishop.png").convert_alpha()
            # convert alpha preserves per pixel transparency
        elif (self.color == 'white'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\whiteBishop.png").convert_alpha()
        else:
            print "Color issue with Bishop"

    def __str__(self):
        return self.color + " bishop"
    
    # returns True or a string error message 
    def validMove(self, board, currentCol, currentRow, destCol, destRow): #row is y value
        #input is string values below values (X Y) are numerical ints
        if board.isOccupied(destCol, destRow) and board.squareDic[destCol + destRow].piece.color == self.color:
                return False, "Can't capture your own piece"
        currentX = colNumber[currentCol]
        currentY = int(currentRow)
        destX = colNumber[destCol]
        destY = int(destRow)
        absX = abs(destX-currentX)
        absY = abs(destY-currentY)
        if (absX == 0 and absY == 0): #doesn't actually move
            return False, "That's not moving!"
        elif destX > 7 or destX < 0 or destY > 7 or destX < 0: #goes off grid
            return False, "You can't move your piece off the grid"
        else: 
            if absX != absY:
                return False, "Bishops cannot move in this way"
            else: #need to ensure that spaces inbetween are unoccupied
                if absX == 1:
                    return True, "" #no spaces in between
                else:
                    x, y = 1, 1 #y corresponds to row, x corresponds to col
                    if currentX > destX:
                        x = -1
                    if currentY > destY:
                        y = -1
                    mag = 1 #magnitude 
                    while mag < absX: #absX = numSpaces inbetween +1
                        if board.isOccupied(colStr(currentX + mag*x), str(currentY + mag*y)):
                            return False, "Bishop cannot leap over other pieces."
                        mag += 1
                    return True, ""
                        
class Queen(Piece):
    def setPic(self):
        if (self.color == 'black'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\BlackQueen.png").convert_alpha()
            # convert alpha preserves per pixel transparency
        elif (self.color == 'white'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\whiteQueen.png").convert_alpha()
        else:
            print "Color issue with Queen"

    def __str__(self):
        return self.color + " queen"
    
    # returns True or a string error message
    def validMove(self, board, currentCol, currentRow, destCol, destRow): #row is y value
        #input is string values below values (X Y) are numerical ints
        if board.isOccupied(destCol, destRow) and board.squareDic[destCol + destRow].piece.color == self.color:
                return False, "Can't capture your own piece"
        currentX = colNumber[currentCol]
        currentY = int(currentRow)
        destX = colNumber[destCol]
        destY = int(destRow)
        absX = abs(destX-currentX)
        absY = abs(destY-currentY)
        if (absX == 0 and absY == 0): #doesn't move
            return False, "That's not moving!"
        elif destX > 7 or destX < 0 or destY > 7 or destX < 0: #goes off grid
            return False, "You cannot move your piece off the grid"
        else: 
            if absX != absY: #not valid for bishop, check Rook Moves
                if currentX == destX:
                    if abs(currentY - destY) == 1: #no spaces in between
                        return True, ""
                    elif currentY < destY:
                        tempY = currentY + 1
                        while tempY < destY:
                            if board.isOccupied(destCol, str(tempY)): # col, row
                                return False, "Queen cannot leap over other pieces."
                            tempY +=1
                        return True, ""
                    else: #currentY > destY, need to decrement tempY
                        tempY = currentY - 1
                        while tempY > destY:
                            if board.isOccupied(destCol, tempY): # col, row
                                return False, "Queen cannot leap over other pieces."
                            tempY -=1
                        return True, ""              
                elif currentY == destY:
                    numToCheck = abs(currentY - destY) #actually numtoCheck +1
                    if numToCheck == 1:
                        return True, "" #no spaces in between
                    sList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                    i = 0
                    s = sList[i]
                    while currentCol != s and destCol != s:
                        i+=1
                        s = sList[i]
                    j = 1
                    while j < numToCheck:
                        if board.isOccupied(sList[i+j], destY):
                            return False, "Queen cannot leap over other pieces."
                        j+=1
                    return True, "" #moving in X direction with no pieces in between
                else:
                    return False, "Queen cannot move in this way" #not valid rook or bishop move
                
                
            else: # absX == absY, so moving like a bishop.
                #need to ensure that spaces inbetween are unoccupied
                if absX == 1:
                    return True, "" #no spaces in between
                else:
                    x, y = 1, 1 #y corresponds to row, x corresponds to col
                    if currentX > destX:
                        x = -1
                    if currentY > destY:
                        y = -1
                    mag = 1 #magnitude 
                    while mag < absX: #absX = numSpaces inbetween +1
                        if board.isOccupied(colStr(currentX + mag*x), str(currentY + mag*y)):
                            return False, "Queen cannot leap over other pieces."
                        mag += 1
                    return True, ""

class King(Piece):
    def setPic(self):
        if (self.color == 'black'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\BlackKing.png").convert_alpha()
            # convert alpha preserves per pixel transparency
        elif (self.color == 'white'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\whiteKing.png").convert_alpha()
        else:
            print "Color issue with King"

    def __str__(self):
        return self.color + " king"
    
    #Returns True, or a string error message  
    def validMove(self, board, currentCol, currentRow, destCol, destRow): #row is y value
        #input is string values, below values (X Y) are numerical ints
        currentX = colNumber[currentCol]
        currentY = int(currentRow)
        destX = colNumber[destCol]
        destY = int(destRow)
        if destX < 0 or destY < 0:
            return False, "Not on board"
        absX = abs(destX-currentX)
        absY = abs(destY-currentY)
        if (absX == 0 and absY == 0): 
            return False, "That's not moving!"
        elif destX > 7 or destX < 0 or destY > 7 or destX < 0: #goes off grid
            return False, "You can't move your piece off the grid!"
        elif absX <= 1 and absY <= 1:
            if board.isOccupied(destCol, destRow) and board.squareDic[destCol + destRow].piece.color == self.color:
                return False, "Can't capture your own piece"
            return True, ""
        else:
            return False, "Kings cannot move in this way"

class Pawn(Piece):
    def __init__(self, color, board, col):
        sprite.Sprite.__init__(self)
        self.color = color
        self.col = col
        self.setPic()
        if color == 'black':
            self.row = '6'
        elif color == 'white':
            self.row = '1'
        else:
            print "Pawn color error"
        self.onBoard = True
        startSquare = board.squareDic[self.col+self.row]
        self.rect = startSquare.get_rect()
        startSquare.piece = self
        
    def setPic(self):
        if (self.color == 'black'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\BlackPawn.png").convert_alpha()
            # convert alpha preserves per pixel transparency
        elif (self.color == 'white'):
            self.image = image.load("C:\Users\Colleen\Pictures\usedInSomething\whitePawn.png").convert_alpha()
        else:
            print "Color issue with Pawn"

    def __str__(self):
        return self.color + " pawn"
    
    #Returns True, or a string error message        
    def validMove(self, board, currentCol, currentRow, destCol, destRow): #row is y value
        
        #input is string values below values (X Y) are numerical ints
        if board.isOccupied(destCol, destRow) and board.squareDic[destCol + destRow].piece.color == self.color:
                return False, "Can't capture your own piece"
        currentX = colNumber[currentCol]
        currentY = int(currentRow)
        destX = colNumber[destCol]
        destY = int(destRow)
        absX = abs(destX - currentX)
      
        if (currentY == destY):
            if absX == 0: #doesn't actually move
                return False, "That's not moving!"
            else: 
                return False, "Pawns can't move directly sideways!"
        elif destX > 7 or destX < 0 or destY > 7 or destY < 0: #goes off grid
            return False, "You can't move your piece off the grid!"

        #WHITE ALWAYS STARTS IN ROWS ZERO AND 1
        elif self.color == 'white':
            if destY - currentY <0:
                return False, "Pawns can't move backwards!"
            elif absX==0:
                if board.isOccupied(destCol, destRow):
                    return False, "Pawn cannot capture directly in front of itself"
                if currentY == 1 and destY == 3:
                    if board.isOccupied(currentCol, 2): #checks square in between
                        return False, "Pawn cannot jump over a piece"
                    return True, ""
                elif destY == currentY +1:
                    return True, ""
                else:
                    return False, "Pawns can't move that far"
            elif absX == 1 and destY - currentY == 1:
                if board.isOccupied(destCol, destRow):
                    return True, ""
                else:
                    return False, "Pawn can only move that way when capturing"
            else:
                return False, "This piece can't move that many spaces now."
            
        elif self.color == 'black':
            if destY - currentY > 0:
                return False, "Pawns can't move backwards!"
            elif absX==0:
                if board.isOccupied(destCol, destRow):
                    return False, "Pawn cannot capture directly in front of itself"
                if currentY == 6 and destY == 4:
                    if board.isOccupied(currentCol, 5): #checks square in between
                        return False, "Pawn cannot jump over a piece"
                    return True, ""
                elif destY == currentY - 1:
                    return True, ""
                else:
                    return False, "Pawns can't move that far"
            elif absX == 1 and destY - currentY == -1:
                if board.isOccupied(destCol, destRow):
                    return (True, "")
                else:
                    return False, "Pawn can only move that way when capturing"
            else:
                return False, "This piece can't move that many spaces now."
        else:
            return False, "Color Error"
