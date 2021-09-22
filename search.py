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

def depthFirstSearch(problem):
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

    #This code implements iterative DFS 
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    #globals
    visited = set()
    solution_path = []
    fringe = util.Stack()

    start = problem.getStartState()
    
    fringe.push(([start, None, 0], [None]))

    #for s in problem.getSuccessors(start):
        #s_with_path = [s,[s[1]]]
        #fringe.push(s_with_path)
    
    while(not fringe.isEmpty()):
        u = fringe.pop()
        node = u[0][0]
        path_to_node = u[1]

        if(problem.isGoalState(node)):
            solution_path = path_to_node
            break

        if(node not in visited):
            visited.add(u[0][0])
            neighbors = problem.getSuccessors(node)

            for v in neighbors: 
                if v not in visited:
                    new_path = path_to_node + [v[1]]
                    fringe.push([v, new_path])

    return solution_path[1::]  
    util.raiseNotDefined

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    #globals
    visited = set()
    solution_path = []
    fringe = util.Queue()

    start = problem.getStartState()
    fringe.push(((start, None, 0), [None]))
    #fringe contents: ([node, action, cost], [path])
    
    while(not fringe.isEmpty()):
        u = fringe.pop()
        node = u[0][0]
        path_to_node = u[1]

        if(problem.isGoalState(node)):
            solution_path = path_to_node
            break
        
        if(node not in visited):
            visited.add(u[0][0])
            neighbors = problem.getSuccessors(node)

            for v in neighbors: 
                if v not in visited:
                    new_path = path_to_node + [v[1]]
                    fringe.push([v, new_path])

    return solution_path[1::]    


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    def getCost(fringeItem):
        return fringeItem[0][2]

    #globals
    visited = set()
    solution_path = []
    fringe = util.PriorityQueueWithFunction(getCost)

    start = problem.getStartState()
    fringe.push(([start, None, 0], [None]))
    
    while(not fringe.isEmpty()):
        u = fringe.pop()
        node = u[0][0]
        path_to_node = u[1]
        curr_cost = u[0][2]

        if(problem.isGoalState(node)):
            solution_path = path_to_node
            break

        if(node not in visited):
            visited.add(u[0][0])
            neighbors = problem.getSuccessors(node)

            for v in neighbors: 
                if v not in visited:
                    (next, action, add_cost) = v
                    new_cost = curr_cost + add_cost
                    new_path = path_to_node + [v[1]]
                    fringe.push([[next, action, new_cost], new_path])

    return solution_path[1::]  

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    def getCost(fringeItem):
        return fringeItem[0][2] + heuristic(fringeItem[0][0], problem=problem)

    #globals
    visited = set()
    solution_path = []
    fringe = util.PriorityQueueWithFunction(getCost)

    start = problem.getStartState()
    fringe.push(([start, None, 0], [None]))
    
    while(not fringe.isEmpty()):
        u = fringe.pop()
        node = u[0][0]
        path_to_node = u[1]
        curr_cost = u[0][2]

        if(problem.isGoalState(node)):
            solution_path = path_to_node
            break

        if(node not in visited):
            visited.add(u[0][0])
            neighbors = problem.getSuccessors(node)

            for v in neighbors: 
                if v not in visited:
                    (next, action, add_cost) = v
                    new_cost = curr_cost + add_cost #+ heuristic(next, problem=problem)
                    new_path = path_to_node + [v[1]]
                    fringe.push([[next, action, new_cost], new_path])

    return solution_path[1::]  
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
