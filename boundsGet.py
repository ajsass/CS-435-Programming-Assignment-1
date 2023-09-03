import xml.etree.ElementTree as ET

#Andrew Sass
#9/1/23
#CS 435 Software Engineering Coding Assessment

#File Description
#This code opens a given XML file and searches for all leaf nodes
# then adds the boundaries of the gui items to a list, then returns that list


'''Finds leaf nodes of an xml (this is mainly for testing so I can see how elementTree works)'''
def FindLeaf(filename):
    tree = ET.parse(filename+'.xml') # initialize tree

    root = tree.getroot()  # get root

    Bounds=[]  #initialize bounds list
    Bounds= leafSearch(root,Bounds) # fill bounds list
    return Bounds   # return bounds list to GUI circler
   




'''recursivly looks at each node given a root, if its a leaf its bounds are added to the list and list is returned '''
def leafSearch(node,boundList):
    if len(node)==0:  # if length = 0 it has no children and is a leaf
        boundList.append(node.attrib.get('bounds')) # add bounds to list
        return boundList # return list
    else:
        for child in node:  # if not a child loop over its children
            leafSearch(child,boundList) # add childs bounds to list
        return boundList # return list





if __name__ == '__main__':
    FindLeaf() #MAIN (FOR TESTING)