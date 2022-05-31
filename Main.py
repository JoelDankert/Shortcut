import keyboard
import time

word = []
shortcut = []

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','ä','ö','ü','ß','1','2','3','4','5','6','7','8','9','0','.',',','#','space','+','-','tab','shift','ctrl','alt','enter']
keystell = ['a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ', 'n ', 'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 'y ','z ','ae','oe','ue','ss','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','0 ','. ',', ','# ','  ','+ ','- ','ta','sh','co','al','en']
keyremove = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1]


keymacropressed = []
                                                                                  
pressed = []
laststatuspressed = []
recordedkeys = ''

time.sleep(1)


def loadfile():
    global word
    global shortcut
    word = []
    shortcut = []


    shortcutfile = open('shortcuts.txt','r')
    lines = shortcutfile.readlines()

    index = 0
    for line in lines:
        if line[0] != '#':
            if line[-1] == '\n':
                line = line[:-1]
            if index % 2 == 0:
                word.append(line)
            else:
                shortcut.append(line)
            index = index + 1

    #print(word)
    #print(shortcut)
            

def addtopressed():
    global pressed
    for i in keys:
        pressed.append(False)
        laststatuspressed.append(False)
        keymacropressed.append(False)

def checkkeys():
    for i,k in enumerate(keys):
        pressed[i] = keyboard.is_pressed(k)
        

def addstrokes():
    global recordedkeys
    for i,k in enumerate(keys):
        if laststatuspressed[i] == False and pressed[i] == True:
            recordedkeys = recordedkeys + keystell[i]
        
def updatelaststate():
    for i,k in enumerate(pressed):
        laststatuspressed[i] = k

def checkpatterns():
    global recordedkeys
    for i,s in enumerate(shortcut):
        if recordedkeys.endswith(s):
            typeword(s,word[i])
            recordedkeys = ''

def checkforremove(remove):
    sum = 0
    for x in range(0,len(remove),2):
        for i in range(0,len(keystell),1):
            if remove[x] + remove[x+1] == keystell[i]:
                sum = sum + keyremove[i]
    return sum

def typeword(remove,add):
    
    for x in range(0,checkforremove(remove)):
        keyboard.send('backspace')

    if add[0] == '&':
         for letter in add:
            if letter == '*':
                time.sleep(0,2)
            else:
                keyindex = keys.index(letter)
                if keymacropressed[keyindex] == False:
                    keyboard.press(letter)
                    keymacropressed[keys.index(letter)] = True
                else:
                    keyboard.release(letter)
                    keymacropressed[keys.index(letter)] = False
    else:
        for letter in add:
            if letter == '*':
                keyboard.send('enter')
            else:
                keyboard.write(letter)
    

loadfile()
addtopressed()
lastbackspace = False
while(True):
    time.sleep(0.01)
    checkkeys()
    addstrokes()
    if keyboard.is_pressed('backspace') and lastbackspace == False and len(recordedkeys) > 0:
        recordedkeys = recordedkeys[:-2]
    checkpatterns()

    #keep at end
    updatelaststate()
    lastbackspace = keyboard.is_pressed('backspace')
