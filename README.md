# Model Proposal for Fuzzy Logic Design Optimization with Design Agents

Conner Goodrum

* Course ID: CMPLXSYS 530,
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2017


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


&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment
_Description of the environment in your model. Things to specify *if they apply*:

* _Dimensionality (e.g. 1D, 2D, etc.): The environment will consist of 2D points (acting as patches) which contain a single function value at that point.
* _List of environment-owned variables (e.g. resources, states, roughness)_
* _List of environment-owned methods/procedures (e.g. resource production, state change, etc.)_


&nbsp; 

### 2) Agents
 
 The agents in the model have the following agent owned variables:
 
* _Type: The agent type, which will define which sort of agent it is (greedy, etc.)
* _Interaction rules: Cases which define what happens when it meets an agent.
* _

The agents in the model have the following agent owned methods/procedures:

* Interact


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

_Describe and list any global parameters you will be applying in your model:

Number of agents: Defined by the number of each type of agent.
Negotation rules: The rules for how votes will be handled.
Fuzzy rule matrix: This is a pre-defined method for the rules activated when the negotiations have ocurred.

_Describe how your model will be initialized_

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
