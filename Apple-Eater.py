from graphics import * 

def main():
    numberOfApples = getInputs()
    win,character1,allTheApples = drawScene(numberOfApples)
    game(win,character1,allTheApples,numberOfApples)

def getInputs():
    appleNumber = eval(input("How many apples do you want:"))
    if appleNumber < 1:
        appleNumber = eval(input("You must have at least one apple:"))
    return appleNumber

def drawScene(numberOfApples):
    win= background()
    character1 = android(win)
    allTheApples = apples(win,numberOfApples)
    return win,character1,allTheApples
   
def game(win,character1,allTheApples,numberOfApples):
    #Opening text
    startText = Text(Point(600,250),"Eat the apples and do not touch the edge")
    startText.setSize(32)
    startText.setFill("white")
    startText.draw(win)
    time.sleep(3)
    startText.undraw()
    startText1 = Text(Point(600,250),"Use the left and right arrow keys to move")
    startText1.setSize(32)
    startText1.setFill("white")
    startText1.draw(win)
    time.sleep(2)
    startText1.undraw()
    
    #Setting the variables
    runGame = True
    specificApple = 0
    won = False
    
    while runGame == True and won == False:
        control(win, character1)
        #Wall collisions
        lHand = character1[3].getCenter()
        if lHand.getX() <= 5:
            for part in character1:
                part.move(600,0)
                runGame = False
        rHand = character1[4].getCenter()
        if rHand.getX() >= 1195:
            for part in character1:
                part.move(-600,0)
                runGame = False
        
        #Eating the apples
        head = character1[0].getCenter()
        allTheApples[specificApple].move(0,0.06)
        ballCenter = allTheApples[specificApple].getCenter()
  
        if distanceBetweenPoints(head, ballCenter) < 25:
            allTheApples[specificApple].undraw()
            specificApple = specificApple +1
        
        elif ballCenter.getY() > 550:
            allTheApples[specificApple].undraw()
            runGame = False
        
        if specificApple == numberOfApples:
            won = True

    if won == True:
        text= Text(Point(600,200),"You Win!!!")
        text.setSize(32)
        text.setFill("white")
        text.draw(win)
        print("Game over")
        time.sleep(1)
        win.close()
    
    if runGame == False:
        text= Text(Point(600,200),"Game over")
        text.setSize(32)
        text.setFill("white")
        text.draw(win)
        print("Game over")
        time.sleep(1)
        win.close()
    
    
#Draw Scene
def background():
    win= GraphWin("Andriod", 1200, 600)
    background = Rectangle(Point(0,0), Point(1200,600))
    background.setFill("skyblue")
    background.draw(win)
    bline = Line(Point(0,550), Point(1200,550))
    bline.setFill("green")
    bline.draw(win)
    leftline1 = Line(Point(1,0), Point(1,550))
    leftline1.setFill("red")
    leftline1.draw(win)
    rightline = Line(Point(1199,0), Point(1199,600))
    rightline.setFill("red")
    rightline.draw(win)
    treestump = Rectangle(Point(550,200), Point(650,550))
    treestump.setFill("saddlebrown")
    treestump.draw(win)
    floor = Rectangle(Point(0,550), Point(1200,600))
    floor.setFill("green")
    floor.draw(win)
    treeLeaves = Circle(Point(600,200),150)
    treeLeaves.setFill("green2")
    treeLeaves.setOutline("green2")
    treeLeaves.draw(win)
    treeLeaves = Circle(Point(755,250),100)
    treeLeaves.setFill("green2")
    treeLeaves.setOutline("green2")
    treeLeaves.draw(win)
    treeLeaves = Circle(Point(455,250),100)
    treeLeaves.setFill("green2")
    treeLeaves.setOutline("green2")
    treeLeaves.draw(win)
    cloud = Circle(Point(1000,150),50)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(955,160),40)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(1050,160),40)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(400,150),50)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(355,160),40)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(450,160),40)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(100,150),50)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(55,160),40)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(150,160),40)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    return win

def android(win):
    head = Circle(Point(600,507),20)
    body = Rectangle(Point(580,510), Point(620,540))
    neck = Rectangle(Point(580,510), Point(620,507))
    leftarm = Rectangle(Point(580,510),Point(570,530))
    rightarm = Rectangle(Point(620,510), Point(630,530))
    leftleg = Rectangle(Point(580,540), Point(590,550))
    rightleg = Rectangle(Point(620,540), Point(610,550))
    eye1 = Circle(Point(590,500),2.5)
    eye2 = Circle(Point(610,500),2.5)
    android = [head,body, neck, leftarm, 
                rightarm, leftleg, rightleg, eye1, eye2]
    for part in android:
        if part == neck:
            part.setFill("white")
            part.draw(win)
        elif part == eye1 or part == eye2:
            part.setFill("white")
            part.draw(win)
        else:
            part.setFill("green2")
            part.draw(win)
    return android

def apples(win,numberOfApples):   
    from random import random
    apple = []
    for i in range(numberOfApples):
        x = random() * 1200
        intX = int(x)
        if intX < 10 or intX >1290:
            intX = 600
        listOfApples = Circle(Point(intX,-10),10)
        apple.append(listOfApples)

    for part in apple:
        part.setFill("red")
        part.draw(win)
    return apple  

#Game
def control(win, character1):
        key = win.checkKey()
        if key == "Left":
            for part in character1:
                part.move(-7,0)
        if key == "Right":
            for part in character1:
                part.move(7,0)

def distanceBetweenPoints(p1, p2):
    import math
    return math.sqrt((p1.getX() - p2.getX()) ** 2 + 
                     (p1.getY() - p2.getY()) ** 2)

main()


