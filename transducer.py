# SI342 TRANSDUCER PROJECT
# SAM FICSOR 271878
# REAGAN DUFFY
# KHUSH THAKOR

import sys

class transducer:
    
    def __init__(self):
        #make the components of a transducer
        self.Q = {0, 1, 2, 3, 4 ,5, 6} # represents states q0 - q5

        #input alphabet
        self.E = ["click", "clickOnCanvas ", "clickRecenterButton", "clickRecenterPane", "clickRecenterTextBox",
            "clickTriChooseButton", "clickTriTypeChoice", "documentReady", "mouseDownVertex", "mouseLeaveCanvas",
            "mouseMove ", "mouseUpCanvas ", "recenterTextChange ", "recenterTextFail", "recenterTextSucc"]

        #output alphabet
        self.G = ["noop", "showTP ", "hideTP ", "resetT ", "showCP ", "hideCP ",
            "checkCT ","errorCT ", "moveC ", "selectV ", "moveV ", "resetV "]

        self.D = {
            (0, 'documentReady'):(1, 'noop'), (1, 'mouseUpCanvas'):(1, 'moveV'),
            (1, 'clickOnCanvas'):(1, 'selectV'), (1, 'mouseLeaveCanvas'):(1, 'resetV'),
            (1, 'mouseDownVertex'):(1, 'moveV'), (1, 'clickRecenterButton'):(3, 'showCP'),
            (1, 'clickTriChooseButton'):(2, 'showTP'), (2, 'clickOnCanvas'):(1, 'hideTP'), (1, 'clickRecenterButton'):(3, 'showCP'),
            (2, 'click'):(1, 'hideTP'), (2, 'clickTriChooseButton'):(1, 'hideTP'),
            (2, 'clickTriChooseButton'):(1, 'resetT'), (2, 'clickRecenterButton'):(3, 'hideTP', 'showCP'),
            (3, 'recenterTextChange'):(1, 'moveCT'), (3, 'click'):(1, 'hideCP'), (3, 'clickRecenterPlane'):(1, 'hideCP'),
            (3, 'recenterTextChange'):(5, 'checkCT'), (5, 'recenterTextSucc'):(1, 'moveC'), (5, 'click'):(1, 'hideCP'),
            (5, 'recenterTextFail'):(6, 'errorCT'), (6, 'recenterTextChange'):(5, 'checkCT'), (3, 'clickTriChooseButton'):(2, 'hideCP', 'showTP'),
            (5, 'clickTriChooseButton'):(2, 'hideCP', 'showTP'), (6, 'clickTriChooseButton'):(2, 'hideCP', 'showTP')
        }
        
        self.S = 0 #start state
        #M = (Q, E, G, D, S)
        self.M = (self.Q, self.E, self.G, self.D, self.S)
    
        

if __name__ == "__main__":
    frgui = open("fromGUI","r")
    togui = open("toGUI","w")
    M = transducer()
    
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
        # Choose action message to respond with
        # response = "noop 0"
        # match msg:
        #     case 'mouseDownVertex':
        #         response = "showCP " + data
        #     case 'mouseLeaveCanvas':
        #         response = "hideCP " + data
        #     case _:
        #         print(f'No handler for: {msg}',file=sys.stderr)
        
        # Respond to GUI - flush to send line immediately!
        print(response + "\n",file=togui,flush=True)
        print(f'Sent({count}): {response}',file=sys.stderr) #4DEBUG!
        
        
        #     #input on this axis
        # self.D = {(0, None):(1,'documentReady 0'), #for multiple symbol output, make a longer tuple and test for length of tuple when printing
        #     (1, 'selectV '):(1, 'clickOnCanvas '), (1, 'moveV '):(1, 'mouseMove ', 'mouseDownVertex '), (1, 'resetV '):(1, 'leaveCanvas 0'),
        #     (1, 'showTP '):(2, 'clickTriChooseButton 0'), (1, 'showCP '):(3, 'clickRecenterButton 0'),
        #     (2, 'hideTP '):(1, 'clickOnCanvas '), (2, 'hideTP '):(1, 'click 0'), (2, 'hideTP '):(1, 'clickTriChooseButton 0'), (2, 'reset '):(1, 'clickTriChoiceType ')
        #     }