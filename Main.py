import keyboard
import time

word = []
shortcut = []

#accounts
word.extend(['joel.dankert@gmail.com','+4917660186268','Ukii#3647','Ukii','xXUkiiXx'])
shortcut.extend(['em#','tel#','dc#','steam#','epic#'])

#programming
#word.extend(['if (True):\n','else:\n','elif:\n','for i in range(0,len(),1):\n','while (True):\n','print('')'])
#shortcut.extend(['if#','else#','elif#','for#','while#','print#'])

#abkürzungen
word.extend(['sorry','nice try','good luck, have fun!','my bad','thank you','no problem','good job'])
shortcut.extend(['sry','nt','glhf','mb','thx','np','gj'])

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','ä','ö','ü','ß','1','2','3','4','5','6','7','8','9','0','.',',','#','space','+','-']
keystell = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','','ä','ö','ü','ß','1','2','3','4','5','6','7','8','9','0','.',',','#',' ','+','-']
#                                                                                                                                       /\ vorrübergehent 'z' entfernt
pressed = []
laststatuspressed = []
recordedkeys = ''

time.sleep(1)

def addtopressed():
    global pressed
    for i in keys:
        pressed.append(False)
        laststatuspressed.append(False)
        
def updatelaststate():
    for i,k in enumerate(pressed):
        laststatuspressed[i] = k

def addstrokes():
    global recordedkeys
    for i,k in enumerate(keys):
        if laststatuspressed[i] == False and pressed[i] == True:
            recordedkeys = recordedkeys + keystell[i]

def checkkeys():
    for i,k in enumerate(keys):
        if keyboard.is_pressed(k):
            pressed[i] = True
        else:
            pressed[i] = False

def typeword(remove,add):
    for x in range(0,len(remove)):
        keyboard.send('backspace')
    keyboard.write(add)
    
def checkpatterns():
    global recordedkeys
    for i,s in enumerate(shortcut):
        if recordedkeys.endswith(s):
            typeword(s,word[i])
            recordedkeys = ''
        

addtopressed()
while(True):
    time.sleep(0.01)
    checkkeys()
    addstrokes()
    checkpatterns()

    #keep at end
    updatelaststate()
