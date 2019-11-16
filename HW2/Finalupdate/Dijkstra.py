'''BFS.py
by Hung Lo
UWNetID: honkuro
Student number: 1926128

Assignment 2, in CET 513, Autumn 2019.
 
This file contains my problem formulation for the problem of
Dijkstra’s algorithm
'''
VERBOSE = True  # Set to True to see progress; but it slows the search.

import sys
import prb5 as Problem



COUNT = None # Number of nodes expanded.
MAX_OPEN_LENGTH = None # How long OPEN ever gets.
SOLUTION_PATH = None # List of states from initial to goal, along lowest-cost path.
TOTAL_COST = None # Sum of edge costs along the lowest-cost path.
BACKLINKS = {} # Predecessor links, used to recover the path.
table=[]
# The value g(s) represents the cost along the best path found so far
# from the initial state to state s.
g = {} # We will use a global hash table to associate g values with states.

class My_Priority_Queue:
  def __init__(self):
    self.q = [] 

  def __contains__(self, elt):

    for pair in self.q:
      if pair[0]==elt: return True
    return False

  def delete_min(self):
    ''' Standard priority-queue dequeuing method.'''
    if self.q==[]: return [] # Simpler than raising an exception.
    temp_min_pair = self.q[0]
    temp_min_value = temp_min_pair[1]
    temp_min_position = 0
    for j in range(1, len(self.q)):
      if self.q[j][1] < temp_min_value:
        temp_min_pair = self.q[j]
        temp_min_value = temp_min_pair[1]  
        temp_min_position = j
    del self.q[temp_min_position]
    return temp_min_pair

  def insert(self, state, priority):
    '''We do not keep the list sorted, in this implementation.'''
    #print("calling insert with state, priority: ", state, priority)

    if self[state] != -1:
      print("Error: You're trying to insert an element into a My_Priority_Queue instance,")
      print(" but there is already such an element in the queue.")
      return
    self.q.append((state, priority))

  def __len__(self):

    return len(self.q)

  def __getitem__(self, state):
    '''This method enables Pythons right-bracket syntax.
    Here, something like  priority_val = my_queue[state]
    becomes possible. Note that the syntax is actually used
    in the insert method above:  self[state] != -1  '''
    for (S,P) in self.q:
      if S==state: return P
    return -1  # This value means not found.

  def __delitem__(self, state):
    #print("In MyPriorityQueue.__delitem__: state is: ", str(state))
    for count, (S,P) in enumerate(self.q):
      if S==state:
        del self.q[count]
        return

  def __str__(self):
    txt = "My_Priority_Queue: ["
    for (s,p) in self.q: txt += '('+str(s)+','+str(p)+') '
    txt += ']'
    return txt

def runDijkstra():
  '''This is an encapsulation of some setup before running
  Dijkstra, plus running it and then printing some stats.'''
  initial_state = Problem.CREATE_INITIAL_STATE()
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH, SOLUTION_PATH, CLOSED,table
  COUNT = 0
  BACKLINKS = {}
  MAX_OPEN_LENGTH = 0
  SOLUTION_PATH = Dijkstra(initial_state)
  print(str(COUNT)+" states expanded.")
  print("The link of each node and its cost: ")
  for s in table:
      print(s)
  for s in CLOSED:
      print("minimize cost to :"+str(s)+" is "+str(g[s]))
      backtraceg(s)

      

def Dijkstra(initial_state):
  '''Dijkstra algorithm.'''
  global g, COUNT, BACKLINKS, MAX_OPEN_LENGTH, CLOSED, TOTAL_COST
  CLOSED = []
  BACKLINKS[initial_state] = None

  OPEN = My_Priority_Queue()
  OPEN.insert(initial_state, 0)
  g[initial_state]=0.0

  while OPEN != []:

    if len(OPEN)>MAX_OPEN_LENGTH: MAX_OPEN_LENGTH = len(OPEN)

    if(len(OPEN)==0):
        return
    (S,P) = OPEN.delete_min()    
    tempCost=P

    CLOSED.append(S)
#    if Problem.GOAL_TEST(S):
#      print(Problem.GOAL_MESSAGE_FUNCTION(S))
#      path = backtraceg(S)
#      TOTAL_COST=P
#      print('Length of solution path found: '+str(len(path)-1)+' edges '+' total cost '+str(TOTAL_COST))
    COUNT += 1
    for op in Problem.OPERATORS:
      if op.precond(S):
       
        new_state = op.state_transf(S)
        result=str(S)+" → "+str(new_state)+" is : "+str(S.edge_Free_flow_time(new_state))
        if not (result in table):
            table.append(result)
        if not ((new_state in CLOSED) or (new_state in OPEN)):
                tempCost=S.edge_Free_flow_time(new_state)
                g[new_state]=g[S]+tempCost
                OPEN.insert(new_state,g[new_state])
                BACKLINKS[new_state] = S
        else:
            tempCost=g[S]+S.edge_Free_flow_time(new_state)
            if  tempCost<g[new_state]:
                forprint=g[new_state]
                g[new_state]=tempCost
                if new_state in OPEN:
                    print("the value change! To "+str(new_state)+" from "+str(forprint)+ " changes to "+str(g[new_state]) )
                    print("original path is: ")
                    backtraceg(new_state)
                    BACKLINKS[new_state] = S
                    print("New path is :")
                    backtraceg(new_state)
                    del OPEN[new_state]
                    OPEN.insert(new_state,g[new_state])
                if new_state in CLOSED:
                    print("the value change! To "+str(new_state)+" from "+str(forprint)+ " changes to "+str(g[new_state]) )
                    print("original path is: ")
                    backtraceg(new_state)
                    OPEN.insert(new_state,g[new_state])
                    CLOSED.remove(new_state)
                    BACKLINKS[new_state] = S
                    print("New path is :")
                    backtraceg(new_state)

                

def print_state_queue(name, q):
  print(name+" is now: ",end='')
  print(str(q))

def backtrace(S):
  global BACKLINKS, g
  path = []

  while S:
    path.append(S)
    S = BACKLINKS[S]
  path.reverse()
  if(len(path)-1>0):
      print(str(path[len(path)-2])+" → "+str(path[len(path)-1])+" is : "+str(g[path[len(path)-1]]-g[path[len(path)-2]]))
  return path

def backtraceg(S):
  global BACKLINKS
  path = []
  while S:
    path.append(S)
    S = BACKLINKS[S]
  path.reverse()
#  print("Solution path: ")
  result=str(path[0])
  for i in range(len(path)):
    if(i!=0):
        result+=" → "+str(path[i])
  print(result)
  return path

def report(open, closed, count):
  print("len(OPEN)="+str(len(open)), end='; ')
  print("len(CLOSED)="+str(len(closed)), end='; ')
  print("COUNT = "+str(count))

if __name__=='__main__':
    runDijkstra()


