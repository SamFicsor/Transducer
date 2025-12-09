# SI342 TRANSDUCER PROJECT
# SAM FICSOR 271878
# REAGAN DUFFY
# KHUSH THAKOR

import sys

class transducer:
    
    def __init__(self, M):
        # #M = (Q, E, G, D, S)
        self.Q,self.E,self.G,self.D,self.S = M
    
        

if __name__ == "__main__":
    frgui = open("fromGUI","r")
    togui = open("toGUI","w")
    
    # Mtuple = (Q, E, G, D, S)
    Mtuple = (
        {0, 1, 2, 3, 4 ,5, 6, 7},
        ["click", "clickOnCanvas ", "clickRecenterButton", "clickRecenterPane", "clickRecenterTextBox",
        "clickTriChooseButton", "clickTriTypeChoice", "documentReady", "mouseDownVertex", "mouseLeaveCanvas",
        "mouseMove ", "mouseUpCanvas ", "recenterTextChange ", "recenterTextFail", "recenterTextSucc"],
        ["noop", "showTP ", "hideTP ", "resetT ", "showCP ", "hideCP ",
            "checkCT ","errorCT ", "moveC ", "selectV ", "moveV ", "resetV "],
        {(0, 'documentReady'):(1, 'noop'), (1, 'mouseUpCanvas'):(1, 'moveV'), (1, 'mouseDownVertex'):(1, 'moveV'), (1, 'clickRecenterButton'):(3, 'showCP'),
        (1, 'clickTriChooseButton'):(2, 'showTP'), (2, 'clickOnCanvas'):(1, 'hideTP'), (1, 'clickRecenterButton'):(3, 'showCP'),(2, 'click'):(1, 'hideTP'), 
        (2, 'clickTriChooseButton'):(1, 'hideTP'), (2, 'clickTriTypeChoice'):(1, 'resetT', 'hideTP'), (2, 'clickRecenterButton'):(3, 'hideTP', 'showCP'), 
        (3, 'recenterTextChange'):(1, 'moveCT'), (3, 'click'):(1, 'hideCP'), (3, 'clickRecenterPlane'):(1, 'hideCP'), (3, 'recenterTextChange'):(5, 'checkCT'),
        (5, 'recenterTextSucc'):(1, 'moveC', 'hideCP'), (5, 'click'):(1, 'hideCP'), (5, 'recenterTextFail'):(6, 'errorCT'), 
        (6, 'recenterTextChange'):(5, 'checkCT'), (3, 'clickTriChooseButton'):(2, 'hideCP', 'showTP'), (5, 'clickTriChooseButton'):(2, 'hideCP', 'showTP'), 
        (6, 'clickTriChooseButton'):(2, 'hideCP', 'showTP'), (5, 'clickOnCanvas'):(1,'moveC', 'hideCP'), (6, 'clickOnCanvas'):(1,'moveC', 'hideCP'),
        (3, 'clickOnCanvas'):(1,'moveC', 'hideCP'), (1, 'mouseDownVertex'):(7, 'selectV'), (7, 'mouseMove'):(7, 'moveV'), (7, 'mouseLeaveCanvas'):(1, 'resetV'), 
        (7, 'clickOnCanvas'):(1, 'noop')},
        0
    )
    
    M = transducer(Mtuple)
    
    currstate = M.S
    count = 0
    while True:
        # Read event message
        try:
            msg,data = frgui.readline().split(maxsplit=1);
        except:
            break
        count += 1
        print(f'Read({count}): {msg} {data}',file=sys.stderr) #4DEBUG!
        
        response = ''
        
        try:
        # make an output for every output character
        # range from 1 because not including the state we're going to
            for i in range(1, len(M.D[(currstate, msg)])): 
                    response = response + M.D[(currstate, msg)][i] + ' ' + data
            currstate = M.D[(currstate, msg)][0] #move to next state
        except KeyError: # for missing transitions, just do a noop
            response = 'noop 0'
        
        # Respond to GUI - flush to send line immediately!
        print(response + "\n",file=togui,flush=True)
        print(f'Sent({count}): {response}',file=sys.stderr) #4DEBUG!
        print(f'currstate: {currstate}')