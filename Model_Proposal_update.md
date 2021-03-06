# Model Proposal for Fuzzy Logic Design Optimization with Design Agents

Conner Goodrum

* Course ID: CMPLXSYS 530,
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2017


_**LS Comments:** I am leaving fewer comments within the proposal here than I am with others since we have met in person, and I am assuming that conversation supersedes a lot of what you have proposed here. If there is anything in particular you would like addressed or to get feedback in the below, however, just let me know._

&nbsp; 
### Goal 
*****
The goal of my model is to simulate the negotiation of design preferences using several design agents. These agents will all have different design preferences on a given function, and will make use of fuzzy logic to activate a set of fuzzy rules, which will translate the negotiated preferences to a preference surface which can be used for optimization. This hopefully will tie the negotiations of the agents to the optimized design point on a pareto front.

&nbsp;  
### Justification
****
Ship design is not only a complicated task, but it also has many complex nuances which often lead to sub-optimal designs, and thus cost over runs. The large number of variables and disciplines to monitor in a design (such as structures, seakeeping, habitability, survivability, powering, maneuvering, etc) coupled with the numerous interacting systems means that throughout a single design there are many designers involved throughout the process. Each designer (or team of designers) will have their own set of goals and have their own idea of an optimal design (depending on which discipline they are designing), and thus the final product becomes a combination of all of them. Design and design processes have been studied in depth, but I would like to create an environment which allows these negotiations to be monitored and studied, and how they relate to the final 'optimal' design surface.

&nbsp; 
### Main Micro-level Processes and Macro-level Dynamics of Interest
****

The key micro-leel processes are the negotiations between the agents. The agents will each be coded with different preferences in mind (for example greedy, lenient, adaptive) and a vote will be created and used to activite the fuzzy rule bank. The hope is that these micro-level negotiations produce vastly different design surfaces, with very different global optima. In this way, the interactions of the negotiations can be linked to the final converged design.

_**LS Comments:** Good overview here. A lot to potentially incorporate into the model at some point, so clarifying in your final writeup which parts of the above you are focusing on first would be good._

&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment

The environment will consist of 2D points (acting as patches) which contain a single function value at that point. This will be carried out for a grid of pre-determined size.

The environment (patches, points) will contain the following variables:
* function_val: Value of the function at that point.
* design_surf_val: Value of the design function surface at that point.

The environment will contain the following methods/sequences:
* calc_function val: Calculate the function value at the point specified.
* update_design_surface: Calculate the design function surface at that point (after the voting procedure).

_**LS Comments:** As discussed, I think that you might be able to think about this in a pretty aspatial way for the time being. In the future, however, I think there are some definite potentials for incorporating notions of a value surface into a more developed version of the model. Specifically, if you look at the "perspective" and "interpretation" landscapes described in Pages "The Difference", I think you will find a lot to draw on._


&nbsp; 

### 2) Agents
 
 The agents in the model have the following agent owned variables:
 
* Type: The agent type, which will define which sort of agent it is (greedy, etc.)
* Interaction rules: Cases which define what happens when it meets an agent (i.e. greedy_vs_greedy).

The agents in the model have the following agent owned methods/procedures:
* Vote: Will contain that agent's vote and preferences.

&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

The interaction topology here will not exist within a spatial-dependent environment. Instead, it will act more along the lines of a genetic algorithm type of interaction environment, where agents are chosen at random and interact with each other. This will occur for every point in the environment.
 
**_Action Sequence_**

_What does an agent, cell, etc. do on a given turn? Provide a step-by-step description of what happens on a given turn for each part of your model_

1. A patch (point) is selected from the environment.
2. 'n' number of agents are randomly selected from the population.
3. Each agent interacts with the other selected agents, and cast their votes depending on their interaction rules.
4. A vote is held between the selected agents.
5. The winning of the vote determines how the preferences are updated for the next round (in the function and fuzy logic sets), as well as what the response surface looks like.

This sequence is continued until every agent in the population has interacted with other agents and have casted a vote.

&nbsp; 


### 4) Model Parameters and Initialization

_Describe and list any global parameters you will be applying in your model:_

Number of agents: Defined by the number of each type of agent.
Negotation rules: The rules for how votes will be handled.
Fuzzy rule matrix: This is a pre-defined method for the rules activated when the negotiations have ocurred.

_Describe how your model will be initialized_

The model will be initialized by creating the patches and the entire grid surface, and calculating the function values on each patch. The agents will also be initialized (according to the numbers of each) with a baseline set of fuzzy logic rules. These rules will be updated at each tick.

_Provide a high level, step-by-step description of your schedule during each "tick" of the model_

(See **_Action Sequence_**)

&nbsp; 

### 5) Assessment and Outcome Measures

_What quantitative metrics and/or qualitative features will you use to assess your model outcomes?_

* The shape of the design surface
* The shape of the pareto front
* Utopian point
* Final trade-off values

&nbsp; 

### 6) Parameter Sweep

_What parameters are you most interested in sweeping through? What value ranges do you expect to look at for your analysis?_

Sweeping through different numbers (and ratios) of each type of agent present.


&nbsp; 


_**LS Comments:** Feel like we talked out a lot more of these details and potentially changes when we met last week, so hopefully that has been clarifying and helped you get a lot of this hammered out further. I am going to strongly advise that you get a first pass version of these ideas (and maybe more specifically, those we talked about when we met) coded up ASAP so you can start working out kinks in your code and figuring out the nitty-gritty specifics of how you are going to computationally implement these ideas for this initial model. I am expecting that you will most likely need to have at least a crude, initial version running by the end of this coming week to make sure that you have time to work out any bugs that come up and generate a set of modeling results to analyze and discuss by the time we get to the end of the semester._
