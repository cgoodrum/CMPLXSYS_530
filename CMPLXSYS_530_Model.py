# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:57:35 2017

@author: cgoodrum
"""

import matplotlib
import matplotlib.pyplot as plt
import random as rd

rd.seed(0)

## Create Agent Class
class Agent(object):
    
    def __init__(self, agent_name, agent_type, agent_range, agent_loc):
        self.agent_name = agent_name
        self.agent_type = agent_type
        self.agent_range = agent_range
        self.agent_loc = agent_loc

## Define Environment Function
def preference_function(x_vals):
    S = [((x-1.0)**2.0 + 1.0) for x in x_vals]
    return S


## --------------------------------------------------

x_vals = range(11)
num_agents = 10


##----------------- MODEL INITIALIZATION--------------

## Initialize Agents
agents = {}
agent_locs = []
for i in range(num_agents):
    agents[i] = Agent(i,"Simple",[-1,1],rd.uniform(min(x_vals),max(x_vals)))
    agent_locs.append(agents[i].agent_loc)
    
#print agents.keys()
#print agents[1].agent_name

##----------------- MODEL RUNNING --------------




##----------------- MODEL DISPLAY--------------

## Display Data
plt.figure(1)
plt.plot(x_vals,preference_function(x_vals))
plt.hold(True)
plt.plot(agent_locs,preference_function(agent_locs),'*')
plt.hold(False)
plt.grid(True)
plt.show