'''
Created on Jan 11th, 2015

@author: davide
'''
import copy
import Queue
import sys

N = 3
GOAL_STATE = (0, 0, False, N, N)

def missionaries_and_cannibals():
    """Solve the "Missionaries and Cannibals" problem
    """
    
    closed = []
    start_state = (N, N, True, 0, 0)
    plan = []
    start_tuple = (0, start_state, plan)
    fringe = Queue.PriorityQueue()
    fringe.put((0, start_tuple));
    while (True):
        if (fringe.empty()):
            return False
    
        tuple = fringe.get();
        priority, a = tuple
        priority, state, plan = a 
        
        if state in closed:
            continue
        
        closed.append(state)
        
        # Test if goal state is reached
        if is_goal_state(state):
            return plan
        
        # Look for successors of current state checking applicability conditions
        # new states are added to the fringe
        L_m, L_c, b, R_m, R_c = state
        next_priority  = priority + 1
        if b:
            # Boat is on the left bank
            if L_m >= 2:
                action = "2m"
                next_state = (L_m - 2, L_c, False, R_m + 2, R_c)
                next_tuple(fringe, plan, action, next_priority, next_state)                    
            
            if L_m >= 1 and L_c >= 1:  
                action = "1m1c"
                next_state = (L_m - 1, L_c - 1, False, R_m + 1, R_c + 1)
                next_tuple(fringe, plan, action, next_priority, next_state)

            if L_m >= 1:  
                action = "1m"
                next_state = (L_m - 1, L_c, False, R_m + 1, R_c)
                next_tuple(fringe, plan, action, next_priority, next_state)

            if L_c >= 1:  
                action = "1c"
                next_state = (L_m, L_c - 1, False, R_m, R_c + 1)
                next_tuple(fringe, plan, action, next_priority, next_state)
                
            if L_c >= 2:  
                action = "2c"
                next_state = (L_m, L_c - 2, False, R_m, R_c + 2)
                next_tuple(fringe, plan, action, next_priority, next_state)
                                    
        else:
            # Boat is on the right bank
            if R_m >= 2:
                action = "2m"
                next_state = (L_m + 2, L_c, True, R_m - 2, R_c)
                next_tuple(fringe, plan, action, next_priority, next_state)                    
            
            if R_m >= 1 and R_c >= 1:  
                action = "1m1c"
                next_state = (L_m + 1, L_c + 1, True, R_m - 1, R_c - 1)
                next_tuple(fringe, plan, action, next_priority, next_state)

            if R_m >= 1:  
                action = "1m"
                next_state = (L_m + 1, L_c, True, R_m - 1, R_c)
                next_tuple(fringe, plan, action, next_priority, next_state)
                
            if R_c >= 1:  
                action = "1c"
                next_state = (L_m, L_c + 1, True, R_m, R_c - 1)
                next_tuple(fringe, plan, action, next_priority, next_state)
                
            if R_c >= 2:  
                action = "2c"
                next_state = (L_m, L_c + 2, True, R_m, R_c - 2)
                next_tuple(fringe, plan, action, next_priority, next_state)
                    
def is_goal_state(state):
    """Check if state is Goal state
    """
    if (state == GOAL_STATE):
        return True
    else:
        return False
    
def is_legal(state):
    """Check if the passed state is legal
    """
    L_m, L_c, b, R_m, R_c = state
    if L_m > 0 and L_c > L_m:
        return False
    
    if R_m > 0 and R_c > R_m:
        return False
    
    return True
    
def next_tuple(fringe, plan, action, next_priority, next_state):
    """Utility to build the next tuple to be added to the fringe
    """
    if not is_legal(next_state):
        return False
    
    next_plan = copy.deepcopy(plan)
    next_plan.append(action)
    next_tuple = (next_priority, next_state, next_plan)
    fringe.put((next_priority, next_tuple))
    
    return True
    
def print_state(state):
    """Print current state of the problem
    """
    L_m, L_c, b, R_m, R_c = state
    s = ""
    for m in range(L_m):
        s = s + "m"
    if L_m > 0 and L_c > 0:
        s = s + ", "
    for m in range(L_c):
        s = s + "c"
        
    s = s + "|"
    if b:
        s = s + "b     |"
    else:
        s = s + "     b|"
        
    for m in range(R_m):
        s = s + "m"
    if R_m > 0 and R_c > 0:
        s = s + ", "
    for m in range(R_c):
        s = s + "c"
        
    print s
    
def print_action(action, b):
    """Print action
    """
    s = ""
    if b:
        s = action + "-->"
    else:
        s = "<--" + action
        
    print "Action: " + action
 
def execute_plan(start_state, plan):
    """Execute the passed plan
    """
    
    print "Start state:"
    print_state(start_state)
    print
    
    next_state = start_state
    
    for action in plan:
        
        if action == "":
            continue
        
        L_m, L_c, b, R_m, R_c = next_state        
        if b:
            if "2m" == action:
                next_state = (L_m - 2, L_c, False, R_m + 2, R_c)
            elif "1m1c" == action:
                next_state = (L_m - 1, L_c - 1, False, R_m + 1, R_c + 1)
            elif "1m" == action:
                next_state = (L_m - 1, L_c, False, R_m + 1, R_c)
            elif "1c" == action:
                next_state = (L_m, L_c - 1, False, R_m, R_c + 1)
            elif "2c" == action:
                next_state = (L_m, L_c - 2, False, R_m, R_c + 2)
        else:
            if "2m" == action:
                next_state = (L_m + 2, L_c, True, R_m - 2, R_c)
            elif "1m1c" == action:
                next_state = (L_m + 1, L_c + 1, True, R_m - 1, R_c - 1)
            elif "1m" == action:
                next_state = (L_m + 1, L_c, True, R_m - 1, R_c)
            elif "1c" == action:
                next_state = (L_m, L_c + 1, True, R_m, R_c - 1)
            elif "2c" == action:
                next_state = (L_m, L_c + 2, True, R_m, R_c - 2)

        print_action(action, b)
        print_state(next_state)
        print
    
    print    
    print "Goal reached."
        
#
# Main program
#
plan = missionaries_and_cannibals()

if plan == False:
    print "No plan found to solve problem."
    sys.exit(-1)    

print "Solution found. Plan consists of %d actions:" % (len(plan))
print plan
print 
print

print "Execution of solving plan:"
start_state = (N, N, True, 0, 0)
execute_plan(start_state, plan)
   