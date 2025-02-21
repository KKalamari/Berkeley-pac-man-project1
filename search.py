# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    path = [] 
    stack = Stack() #creat the main stack for the dfs 
    node = problem.getStartState()        
    visited = []

    if problem.isGoalState(node): #check if the first node is also the wanted node 
        return path

    stack.push([node,path])

    while stack.isEmpty() != 1:    
        node, steps = stack.pop()   #pop a node and the steps for the node

        if problem.isGoalState(node): #if the node is the goal then return it's steps
                return steps
        
        if node not in visited:  #if it's the first time it's visited then add it to the list
            visited.append(node)
            
            succs= problem.getSuccessors(node)
            for next_node,next_step,cost in succs:  #then push all of it's succesors that have not been visited with it's corresponding steps
                if next_node not in visited:
                    stack.push([next_node,steps+ [next_step]])
        
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
      
    path = [] 
    queue = Queue() #creat the main queue for the bfs 
    node = problem.getStartState()        
    visited = []

    if problem.isGoalState(node): #check if the first node is also the wanted node 
        return path

    queue.push([node,path])

    while queue.isEmpty() != 1:    
        node, steps = queue.pop()   #pop a node and the steps for the node

        if problem.isGoalState(node): #if the node is the goal then return it's steps
                return steps
        
        if node not in visited:  #if it's the first time it's visited then add it to the list
            visited.append(node)
            
            succs= problem.getSuccessors(node)
            for next_node,next_step,cost in succs:  #then push all of it's succesors that have not been visited with it's corresponding steps
                if next_node not in visited:
                    queue.push([next_node,steps+ [next_step]])
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    path = [] 
    queue = PriorityQueue() #creat the main prorityqueue for the bfs 
    node = problem.getStartState()        
    visited = []

    if problem.isGoalState(node): #check if the first node is also the wanted node 
        return path

    queue.push([node,[]],0)

    while queue.isEmpty() != 1:    
        node, steps = queue.pop()   #pop a node and the steps for the node

        if problem.isGoalState(node): #if the node is the goal then return it's steps
                return steps
        
        if node not in visited:  #if it's the first time it's visited then add it to the list
            visited.append(node)
            
            succs= problem.getSuccessors(node)
            for next_node,next_step,cost in succs:  #then push all of it's succesors that have not been visited with it's corresponding steps and cost
                the_steps = steps + [next_step]
                the_cost = problem.getCostOfActions(the_steps)
                if next_node not in visited:                    
                    queue.push([next_node, the_steps], the_cost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    path = [] 
    queue = PriorityQueue() #creat the main prorityqueue for the bfs 
    node = problem.getStartState()        
    visited = []

    if problem.isGoalState(node): #check if the first node is also the wanted node 
        return path

    queue.push([node,[],0],0)

    while queue.isEmpty() != 1:    
        node,steps,co = queue.pop()   #pop a node and the steps for the node

        if problem.isGoalState(node): #if the node is the goal then return it's steps
                return steps
        
        if node not in visited:  #if it's the first time it's visited then add it to the list
            visited.append(node)
            
            succs= problem.getSuccessors(node)
            for next_node,next_step,cost in succs:  #then push all of it's succesors that have not been visited with it's corresponding steps and cost
                the_steps = steps + [next_step]
                the_cost = problem.getCostOfActions(the_steps)
                if next_node not in visited:                    
                    queue.push([next_node, the_steps, the_cost],the_cost + heuristic(next_node,problem))
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
