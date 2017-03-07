from xml.dom import minidom
from time import sleep

def changeMap(i):
#  1
#2   0
#  3
    def waitMap():
        while not exists("chargement-2.png"):
            sleep(0.1)
        while exists("chargement-2.png"):
            sleep(0.1)
    
    def top():
        click(Location(644, 63))    
        
    def bottom():
        click(Location(688, 750))
    
    def left():
        click(Location(123, 383))
    
    def right():
        click(Location(1154, 418))

    if(i=="0"):
        right()
    elif(i=="1"):
        top()
    elif(i=="2"):
        left()
    elif(i=="3"):
        bottom()
    else:
        popup("erreur")
    waitMap()

def loadChemin():
    directions = []
    xmldoc = minidom.parse("chemin.xml")    
    if xmldoc.toxml() == "":
        popup("erreur chargement chemin")
        return
    maps = xmldoc.getElementsByTagName("map")
    for map in maps:
        direction = map.childNodes[1].firstChild.nodeValue
        directions.append(direction)
    popup("Chemin chargé")
    return directions



def coupe():
    img = "1488879785774.png"
    
    
    test = exists(img)
    prevClick = (0,0)
    newClick = (0,0)
   
   
    while( test ):
        hover(img)
        prevClick = newClick
        newClick = Env.getMouseLocation()
        if(prevClick != newClick): 
           click(img) 
        sleep(1)
        levelup()
        plein()
        test = exists(img)


def miseEnVente():
    click("1488880250950.png")
    while(exists("1488881154036.png")):
        click("1488881194120.png")        
        sleep(1)
        click("1488880250950.png")
            
            
    sleep(1)
    click("1488880263983.png")
    sleep(1)
    click("1488880844810.png") 
    sleep(1)
    Region(383,66,375,408)
    click("1488880566263.png")   
    sleep(1)
    click("1488880350226.png")
    sleep(1)
    click("1488880356025.png")
    sleep(1)
    click("1488880364614.png")
    sleep(1)
    click("1488880374744.png")
    sleep(1)
    click("1488880425832.png")
    sleep(1)
    click("1488880441413.png")
    sleep(1)
    click("1488880455398.png")
    
    
    
    
    
    

def plein():
    if exists("plein.png"):
        miseEnVente()
        

def levelup():
    if exists("1488812866850.png"):
        click("1488812885683.png")


def main():
    directions = loadChemin()
    
    for i in directions:
        coupe()
        changeMap(i)


main()

