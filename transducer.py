# SI342 TRANSDUCER PROJECT
# SAM FICSOR 271878
# REAGAN DUFFY 271614
# KHUSH THAKOR 276372

import sys

class transducer:
    
    def __init__(self, M):
        # M = (Q, E, G, D, S), but we only will use D and S here, since the way we did the transitions
        # makes Q, E, and G redundant code we don't need
        self.D,self.S = M
        self.currstate = self.S
    
if __name__ == "__main__":
    frgui = open("fromGUI","r")
    togui = open("toGUI","w")
    
    # Mtuple = (Q, E, G, D, S)
    Mtuple = ( 
        # considered doing this like how the dfa lab we did worked, where we pass in a set of transitions and make them into a map,
        # but the fact that a transducer can have multiple output 'characters' for a single input makes this impractical, 
        # because there is no guarantee how many output characters there will be, and making a map from 3 lists would be super inefficient, so we just made a map from the start
        # formatted as: (p, x):(q, y+), where p is the current state, x is the input character, q is the destination state, y+ is one or more output characters
        # there's also a lot of 'noop' transitions that stay in the same state and don't do anything, this is to make sure that ERROR messages
        # are actually useful, not having those transitions doesn't actually affect the program, but they make debugging better
        {(0, 'documentReady'):(1, 'noop'), (1, 'clickRecenterButton'):(3, 'showCP'), (1, 'mouseMove'):(1, 'noop'), (1, 'click'):(1, 'noop'), 
        (1, 'mouseLeaveCanvas'):(1, 'noop'), (2, 'mouseMove'):(2, 'noop'), (2, 'mouseLeaveCanvas'):(2, 'noop'), (3, 'mouseMove'):(3, 'noop'), 
        (3, 'mouseLeaveCanvas'):(3, 'noop'), (6, 'mouseMove'):(6, 'noop'), (6, 'mouseLeaveCanvas'):(6, 'noop'), (6, 'mouseUpCanvas'):(6, 'noop'),
        (1, 'clickTriChooseButton'):(2, 'showTP'), (2, 'clickOnCanvas'):(1, 'hideTP'),(2, 'click'):(1, 'hideTP'), (1, 'mouseUpCanvas'):(1, 'noop'),
        (2, 'clickTriChooseButton'):(1, 'hideTP'), (2, 'clickTriTypeChoice'):(1, 'resetT', 'hideTP'), (2, 'clickRecenterButton'):(3, 'hideTP', 'showCP'), 
        (3, 'click'):(1, 'hideCP'), (3, 'clickRecenterPlane'):(1, 'hideCP'), (3, 'recenterTextChange'):(5, 'checkCT'), (1, 'clickOnCanvas'):(1, 'noop'),
        (5, 'recenterTextSucc'):(1, 'moveC', 'hideCP'), (5, 'click'):(1, 'hideCP'), (5, 'recenterTextFail'):(6, 'errorCT'), 
        (6, 'recenterTextChange'):(5, 'checkCT'), (3, 'clickTriChooseButton'):(2, 'hideCP', 'showTP'), (5, 'clickTriChooseButton'):(2, 'hideCP', 'showTP'), 
        (6, 'clickTriChooseButton'):(2, 'hideCP', 'showTP'), (5, 'clickOnCanvas'):(1,'moveC', 'hideCP'), (6, 'clickOnCanvas'):(1,'moveC', 'hideCP'),
        (3, 'clickOnCanvas'):(1,'moveC', 'hideCP'), (1, 'mouseDownVertex'):(4, 'selectV'), (4, 'mouseMove'):(4, 'moveV'), (4, 'mouseLeaveCanvas'):(1, 'resetV'), 
        (4, 'clickOnCanvas'):(1, 'noop')},
        0 #start state
    )
    
    #make a new transducer from our tuple
    M = transducer(Mtuple)
    
    # didn't change this part from the gift code
    count = 0
    while True:
        # Read event message
        try:
            msg,data = frgui.readline().split(maxsplit=1);
        except:
            break
        count += 1
        print(f'Read({count}): {msg} {data}',file=sys.stderr) #4DEBUG!
        
        #for each loop, the response gets reset to empty
        response = ''
        
        try:
        # make an output for every output character
        # range from 1 because not including the state we're going to (index 0)
            for i in range(1, len(M.D[(M.currstate, msg)])): 
                    response = response + M.D[(M.currstate, msg)][i] + ' ' + data
            M.currstate = M.D[(M.currstate, msg)][0] #move to next state
        except KeyError: # for missing transitions, print an error message to stderr
            print(f'ERROR! Unexpected event message {msg} while in state {M.currstate}',file=sys.stderr)
        
        # Respond to GUI - flush to send line immediately!
        print(response + "\n",file=togui,flush=True)
        print(f'Sent({count}): {response}',file=sys.stderr) #4DEBUG!
        print(f'currstate: {M.currstate}', file=sys.stderr) #4DEBUG as well :)