### Fraternity Brother Building Script 1.0
### Written by: Ryan Caldwell

import random

brother_names = ["Nick Orbash", "Adam Rumer", "Dylan Rhodes", "Nick Contestabile", "Ryan Naylor", "Pat Loedding", "Andy Howland",
                 "Justin Hopf", "Paul Hedzik", "Chris Gordon", "Dillon Frazier", "Bryan Deal", "Logan Campbell", "Jake Haberman",
                 "Seth Stinson", "Rex Gregory", "Chris DeSanti", "Jose Arocho", "Brooks Truel", "Shane Schliefer", "Brandon Kraeer",
                 "Ian Besong", "Connor Himich", "Ryan Caldwell", "Brandon Fuhs", "Dan Kaufman", "Alex Hvizdos", "Ashley Felmlee"]

numBrothers = len(brother_names)

#Function if there is a group of three necessary (odd number of brothers)
def makeGroupOfThree():
    print "Group of three:"
    brotherCount = 1
    while(brotherCount < 4):
        randomBrother = random.randint(0, len(brother_names)-1)
        print "Brother #" + str(brotherCount) + ": " + brother_names[randomBrother]
        del brother_names[randomBrother]
        brotherCount+=1
    print "\n"


def getBrotherPairs():
    while( len(brother_names) > 0 ):
        print "Brother pair:"
        count = 1
        while(count <= 2):
            randomBrother = random.randint(0, len(brother_names)-1)
            print "Brother " + str(count) + ": " + brother_names[randomBrother]
            del brother_names[randomBrother]
            count+=1
        print "\n"

#Main method - 
if __name__ == "__main__":
    print "------- Brother Building Script: Version 1.0 ------"
    print "Number of brothers in (Chapter name) chapter: " + str(len(brother_names)) + "\n"
    if( len(brother_names) % 2 != 0 ): #if there are an odd number of brothers, make a group of three
        makeGroupOfThree()
    getBrotherPairs()
