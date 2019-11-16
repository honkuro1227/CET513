'''prb5.py
("Route Planning for option1)
'''
#<METADATA>
SOLUZION_VERSION = "2.0"
PROBLEM_NAME = "Mincost Flow"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['Hung Lo']
PROBLEM_CREATION_DATE = "28-Oct-2019"

#<COMMON_DATA>
STARTING_Node = "1"
DESTINATION_Node = "6"
STATES = {}

ADJ = {}
ADJ['1'] = ['2','3']
ADJ['2'] = ['3','4']
ADJ['3'] = ['2','5']
ADJ['4'] = ['3','5','6']
ADJ['5'] = ['4']
ADJ['6'] = ['5']


Free_flow_time = {}
Free_flow_time['1'] = {'2':2,'3':8}
Free_flow_time['2'] = {'3':5,'4':3}
Free_flow_time['3'] = {'2':6,'5':0}
Free_flow_time['4'] = {'3':1,'5':7,'6':6}
Free_flow_time['5'] = {'4':4}
Free_flow_time['6'] = {'5':2}

#</COMMON_DATA>

#<COMMON_CODE>

class State():

  def __init__(self, name="no name yet"):

    self.name = name

  def __eq__(self,s2):
    #print("In State.__eq__: s2 is ", str(s2))
    return self.name==s2.name

  def __str__(self):
    return self.name

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State()
    news.name = self.name
    return news 

  def ith_neighbor_exists(self,i):
    '''Tests whether there are enough adjacent cities
    to go to the ith.'''
    return len(ADJ[self.name])>i

  def move(self,i):
    '''Assuming it's legal to transition to the ith neighbor,
    this does it.'''
    neighbor = STATES[ADJ[self.name][i]]
    return neighbor

  def edge_Free_flow_time(self, s2):
    return Free_flow_time[self.name][s2.name]

def goal_test(s):
  return s.name==DESTINATION_Node

def goal_message(s):
  return "finding a route to "+DESTINATION_Node+" !"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

def create_all_states():
  for name in ADJ.keys():
    STATES[name]=State(name)

create_all_states()
#</COMMON_CODE>

#<INITIAL_STATE>
CREATE_INITIAL_STATE = lambda : STATES[STARTING_Node]
#</INITIAL_STATE>

#<OPERATORS>

OPERATORS = [Operator(
  "Go to neighboring city number "+str(i),
  lambda s, i1=i: s.ith_neighbor_exists(i1),
  lambda s, i1=i: s.move(i1))
             for i in range(3)] 
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

def h(s):
    return 0
def setgoal(goals):
    global DESTINATION_Node
    DESTINATION_Node = str(goals)