
import boundsGet as bG
import boxDraw as bD
import os
#Andrew Sass
#9/1/23
#CS 435 Software Engineering Coding Assessment

#File Description
#This code loops through all files in a directory,
# finds a pair of xml & png files, 
#finds bounds of leaf nodes in xml
# and creates a modified screenshot with the leaf level GUI elements in a highlighted box

'''Main'''
if __name__ == '__main__':
    #bounds= bG.FindLeaf()
    #bD.drawBounds(bounds)
    directoryList = os.listdir()



    xmlList=[] # list of xml files
    for file in directoryList: #go through all files
        if file[-3:] == 'xml': # if ends in xml
            xmlList.append (file[:-4]) # save name (not ending)
  

    pairList = [] # list of xml png pairs
    for file in xmlList:
        if file+".png" in directoryList: #if there is a png with same name of an xml file add to list (prevents errors with xml files without a screenshot or screenshots without an xml)
            pairList.append( file)




    for name in pairList:  #for each pair
        bounds= bG.FindLeaf(name) # find leaf bounds
        bD.drawBounds(bounds,name) # draw leaf bounds


    