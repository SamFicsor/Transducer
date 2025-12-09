# SI342 TRANSDUCER PROJECT
# SAM FICSOR 271878
# REAGAN DUFFY
# KHUSH THAKOR

import sys

class transducer:
    #make the components of a transducer
    Q = {0, 1, 2, 3, 4 ,5, 6} # represents states q0 - q5
    #input alphabet
    E = ["noop 0", "showTP ", "hideTP ", "resetT ", "showCP ", "hideCP ",
         "checkCT ","errorCT ", "moveC ", "selectV ", "moveV ", "resetV "]
    #output alphabet
    G = ["click 0", "clickOnCanvas ", "clickRecenterButton 0", "clickRecenterPane 0", "clickRecenterTextBox 0",
         "clickTriChooseButton 0", "clickTriTypeChoice ", "documentReady 0", "mouseDownVertex", "mouseLeaveCanvas 0",
         "mouseMove ", "mouseUpCanvas ", "recenterTextChange ", "recenterTextFail 0", "recenterTextSucc "]
        #input on this axis
    D = {(0, None):(1,'documentReady 0'), #for multiple symbol output, make a longer tuple and test for length of tuple when printing
         (1, 'selectV '):(1, 'clickOnCanvas '), (1, 'moveV '):(1, 'mouseMove ', 'mouseDownVertex '), (1, 'resetV '):(1, 'leaveCanvas 0'),
         (1, 'showTP '):(2, 'clickTriChooseButton 0')}
    S = 0 #start state
    #M = (Q, E, G, D, S)
    M = ()

if __name__ == "__main__":
    frgui = open("fromGUI","r")
    togui = open("toGUI","w")
    
    count = 0
    while True:
        # Read event message
        try:
            msg,data = frgui.readline().split(maxsplit=1);
        except:
            break
        count += 1
        print(f'Read({count}): {msg} {data}',file=sys.stderr) #4DEBUG!

        # Choose action message to respond with
        response = "noop 0"
        match msg:
            case 'mouseDownVertex':
                response = "showCP " + data
            case 'mouseLeaveCanvas':
                response = "hideCP " + data
            case _:
                print(f'No handler for: {msg}',file=sys.stderr)
        
        # Respond to GUI - flush to send line immediately!
        print(response + "\n",file=togui,flush=True)
        print(f'Sent({count}): {response}',file=sys.stderr) #4DEBUG!