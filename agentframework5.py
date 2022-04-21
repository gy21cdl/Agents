# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:36:52 2022

@author: clambert

agentframework5 relateds to the "Agents!" practical and should be used with 
the model5 file.

Directions:
1. Save model5 and agentframework5 in the same directory location
2. Run model5

"""

#Imported modules
import random


#Define "Agent" class
class Agent():
    
    #generate random x & y values
    def __init__ (self):
        """
       Parameters
       ----------
       environment :
           __init__ creates random starting values for x & y between 0 and 99.

       Returns
       -------
       random starting values
        
        """
        self.x = random.randint (0,99) #random values for x
        self.y = random.randint (0,99) #random values for y
        #print (self.x) # test
        #print (self.y) # test
    
    #moves the agents
    def move (self):
        """
        move takes the values generated in __init__ and moves them one step

        Returns
        -------
        Returns new values moved by one step
        
        """
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:       
            self.y = (self.y - 1) % 100

    pass

