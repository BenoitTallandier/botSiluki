from xml.dom import minidom

def loadChemin():
    directions = []
    xmldoc = minidom.parse("chemin.xml")
    maps = xmldoc.getElementsByTagName("map")
    for map in maps:
        direction = map.childNodes[1].firstChild.nodeValue
        directions.append(direction)
    return directions

directions = loadChemin()
