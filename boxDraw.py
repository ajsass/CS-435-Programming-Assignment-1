from PIL import Image, ImageDraw
import os

#Andrew Sass
#9/1/23
#CS 435 Software Engineering Coding Assessment

#File Description
#This code opens a given PNG filename and draws boxes given a list of corner coordinates

'''given a list of bounds and a png filename, draws said bounds on the png'''
def drawBounds(bounds, filename):
    sc = Image.open(filename+'.png')
    draw = ImageDraw.Draw(sc) 
    for item in bounds: # loops through all bounds
        drawBox(item,draw)
    
    dir_path = os.path.abspath(os.path.dirname(__file__)) # get path
    filename = filename+'ANNOTATED.png' # set file name
    sc.save(os.path.join(dir_path, filename))# Save the image in the same folder as the Python file





'''given a string in format "[x,y][xx,yy]", returns a 2d list [[x,y],[xx,yy]]  '''
def parseString(string):
    string = string.replace("[", "") #removes both [s
    string = string [:-1] #removes ending ]
    string = string.split(']') # splits into list ['x,y','xx,yy']
    out= [] # out list
    for item in string:
        out.append(item.split(",")) # splits into [[x,y],[xx,yy]]
    return out #returns




'''Draws box given coordinates'''
def drawBox(item,draw):
    item = parseString(item) # turns string into list
    x = int(item[0][0]) #Casts to ints and makes things easier to understand
    y = int(item[0][1])
    xx = int(item[1][0])
    yy = int(item[1][1])
    draw.line((x, y,xx, y), fill=(255, 255, 0), width=7) #top of box
    draw.line((x, y,x, yy), fill=(255, 255, 0), width=7) # Lside
    draw.line((xx, yy,xx, y), fill=(255, 255, 0), width=7)#R side
    draw.line((xx, yy,x, yy), fill=(255, 255, 0), width=7)#Bottom