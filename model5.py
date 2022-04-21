# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:08:33 2022

@author: clambert

model5 relateds to the "Agents!" practical and should be used with 
the agentframework5 file.

Directions:
1. Save model5 and agentframework5 in the same directory location
2. Run model5

Expected outputs:
1. Scatter chart of agents, coloured individually in a seperate window
2. "Finished" printed on closing the seperate window.
"""

#Imported modules
import random
import operator
import matplotlib.pyplot
import agentframework5 #link to agentframework5.py


a = agentframework5.Agent()
#a. __init__()
a. move ()
#print(a.y, a.x) #test agentframework


#distance_between method - calcualtion used for distance at bottom of code
def distance_between(agents_row_a, agents_row_b):
    """
    distance_between calculates between the two sets of y and x values

    Parameters
    ----------
    agents_row_a : integer
        first row.
    agents_row_b : integer
        second row.

    Returns
    -------
    integer
        value represented a stright line between a and b.

    """
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5


num_of_agents = 10 #changable value
num_of_iterations = 100 # changable value
agents = [] #Creates a new empty list for agents


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework5.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()


#returns graphical results
matplotlib.pyplot.xlim(0, 99) #x axis
matplotlib.pyplot.ylim(0, 99) #y axis
for i in range(num_of_agents): #created and moved agents based on number of agents
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y) #plot scatter of agents
matplotlib.pyplot.show() #show window


#returns distance based on calcuation within the disctnce_between method above
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        #print (distance) #test - distance between all agents

# done marker
print ("finished")

