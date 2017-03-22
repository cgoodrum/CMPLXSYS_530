# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:57:35 2017

@author: cgoodrum
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random as rd
import numpy as npy
import pylab as PL


rd.seed(0)

## Create Agent Class
class Agent(object):
    
    def __init__(self, _name, _type, _range, _loc, _mem):
        self._name = _name
        self._type = _type
        self._range = _range
        self._loc = _loc
        self._mem = _mem
        
## Define Functions
def preference_function(x_vals):
    
    if isinstance(x_vals,list) == True:    
        S = [((x-1.0)**2.0 + 1.0) for x in x_vals]
    else:
        S = ((x_vals-1.0)**2.0 + 1.0)
        
    return S

def preference_function_slope(x_val,x_step):
    pref_func_val = preference_function(x_val)
    pref_func_val_min = preference_function(x_val-x_step)
    S = (pref_func_val - pref_func_val_min)/(x_step)
    return S

def grad_l2_norm(x_vals,x_step):
    pref_gradient_vect = preference_function_slope(x_vals,x_step)
    return npy.linalg.norm(pref_gradient_vect)

def local_value_membership(agent):
    view_min = agent._loc - agent._range
    view_max = agent._loc + agent._range
    local_vals = npy.linspace(view_min,view_max,1000)
    
    local_pref_func = preference_function(local_vals)
    local_val_min = min(local_pref_func)
    local_val_max = max(local_pref_func)
    local_val_mid = 0.5*(local_val_max - local_val_min) + local_val_min
    
    # ADD CODE HERE
    

def local_slope_membership(agent):
    view_min = agent._loc - agent._range
    view_max = agent._loc + agent._range
    local_vals = npy.linspace(view_min,view_max,1000)
    
    local_pref_slope = [preference_function_slope(val,0.00001) for val in local_vals]
    local_slope_min = min(local_pref_slope)
    local_slope_max = max(local_pref_slope)
    local_slope_mid = 0.5*(local_slope_max - local_slope_min) + local_slope_min  
    
    # ADD CODE HERE
    
    
    
    
def global_value_membership(agents):

    global_pref_func = preference_function(x_vals)
    global_val_min = min(global_pref_func)
    global_val_max = max(global_pref_func)
    global_val_mid = 0.5*(global_val_max - global_val_min) + global_val_min
          
    for i in range(len(agents)):
        agent_val = preference_function(agents[i]._loc)
                
        if agent_val <= global_val_mid:
            agents[i]._mem['High'] = 1 + (global_val_min - agent_val)/(0.5*(global_val_max - global_val_min))
            agents[i]._mem['Med'] = (agent_val - global_val_min)/(0.5*(global_val_max - global_val_min))
            agents[i]._mem['Low'] = 0  
        else:
            agents[i]._mem['High'] = 0
            agents[i]._mem['Med'] = (global_val_max - agent_val)/(0.5*(global_val_max - global_val_min))
            agents[i]._mem['Low'] = 1 + (agent_val - global_val_max)/(0.5*(global_val_max - global_val_min))
            
## --------------------------------------------------
## --------------------------------------------------

global grid_min, grid_max, num_steps, num_agents, time, x_vals

grid_min = -2
grid_max = 10
num_steps = 1000
num_agents = 10
x_vals = npy.linspace(grid_min,grid_max,num_steps)


    
##----------------- MODEL INITIALIZATION--------------

def init():
    ## Initialize Agents
    global time, agent_locs, agents
    time = 0
    agents = {}
    agent_locs = []
    for i in range(num_agents):
        agents[i] = Agent(i,"Simple", 1.0, rd.uniform(min(x_vals), max(x_vals)),{"High": 0.0, "Med": 0.0, "Low": 1.0})
        agent_locs.append(agents[i]._loc)

        
##----------------- MODEL DISPLAY--------------

def draw():
    PL.cla()
    PL.plot(x_vals,preference_function(x_vals))
    PL.hold(True)
    PL.plot(agent_locs,preference_function(agent_locs),'*')
    PL.hold(False)
    PL.grid(True)
    PL.title('t = ' + str(time)) 
    

##----------------- MODEL RUNNING --------------

def step():
    global time, agent_locs, agents
    
    print " "
    global_value_membership(agents)
    print " "
    
    for i in range(num_agents):
        print agents[i]._mem
    
    
    
    time = time + 1

 
def run():
    init()
    step()
    draw()

    

import pycxsimulator
pycxsimulator.GUI().start(func=[init, draw, step])
