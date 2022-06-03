import keyboard
import mouse
import time
import os

word = []
shortcut = []
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','ä','ö','ü','ß','1','2','3','4','5','6','7','8','9','0','.',',','#','space','+','-','tab','shift','ctrl','alt','enter','win']
keystell = ['a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ', 'n ', 'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 'y ','z ','ae','oe','ue','ss','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','0 ','. ',', ','# ','  ','+ ','- ','ta','sh','co','al','en','wi']
keyremove = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0]
keymacropressed = [] #for macros: list for checking which keys are held down (simulated)
pressed = [] #holds which keys are pressed
laststatuspressed = [] #holds which keys were pressed last frame
recordedkeys = '' #records keypresses in variable using last and current status

def loadfiles(): #loads files in same folder ending with '*.short'.
    word = []
    shortcut = []

    
    print('checking folder...')
    for filename in os.listdir(os.getcwd()):
        l = len(filename)
        print('checking file: '+filename)
        if filename[l - 6:] == '.short':
            print('found \'.short\' file: '+filename)
            loadfilename(filename)
        
    

def loadfilename(shortcutfilename):
    global word
    global shortcut
    
    print('loading file: '+shortcutfilename)
    
    shortcutfile = open(shortcutfilename,'r')
    
    lines = shortcutfile.readlines()
    print('reading lines')
    index = 0
    for line in lines:
        if line[0] != '#':
            if line[-1] == '\n':
                line = line[:-1]
            if index % 2 == 0:
                word.append(line)
                print('appended word: '+line)
            else:
                shortcut.append(line)
                print('appended shortcut: '+line)
            index = index + 1

def addtopressed(): #extends all lists to full.
    global pressed
    print('extending lists')
    for i in keys:
        print('extended: '+i)
        pressed.append(False)
        laststatuspressed.append(False)
        keymacropressed.append(False)

def checkkeys(): #checks keys and edits pressed list.
    for i,k in enumerate(keys):
        pressed[i] = keyboard.is_pressed(k)
        
def addstrokes(): #checks pressed and laststatuspressed to update strokes.
    global recordedkeys
    for i,k in enumerate(keys):
        if laststatuspressed[i] == False and pressed[i] == True:
            recordedkeys = recordedkeys + keystell[i]
        
def updatelaststate(): #sets last frame of keystrokes.
    for i,k in enumerate(pressed):
        laststatuspressed[i] = k

def checkpatterns(): #checks recorded keystrokes for shortcut patterns, executes the according command.
    global recordedkeys
    for i,s in enumerate(shortcut):
        if recordedkeys.endswith(s):
            print('detected pattern: ' + s)
            typeword(s,word[i])
            print('resetting typed keys...')
            recordedkeys = ''

def typeword(remove,add): #types or executes command and removes typted keys.
    global keymacropressed
    for kmp in keymacropressed:
        kmp = False
    
    for x in range(0,checkforremove(remove)):
        keyboard.send('backspace')
        print('removed key')

    if add[0] == '&':
        print('executing macro')
        addmacro(add)
    else:
        print('typing text')
        addtext(add)


def checkforremove(remove): #checks how many keys need to be removed to delete shortcut.
    sum = 0
    for x in range(0,len(remove),2):
        for i in range(0,len(keystell),1):
            if remove[x] + remove[x+1] == keystell[i]:
                sum = sum + keyremove[i]
    return sum

def addtext(add): #types text
    for letter in add:
        if letter == '*':
            print('sleeping...')
            time.sleep(0.1)
        elif letter == '%':
            print('creating new line')
            keyboard.send('enter')
        else:
            print('writing letter: '+letter)
            keyboard.write(letter)

def addmacro(add): #execute macro
    global keymacropressed
    add = add[1:]
    for i in range(0,len(add),2):
        letter = add[i] + add[i+1]
        if letter == '* ':
            print('sleeping...')
            time.sleep(0.1)
        else:
            keyindex = keystell.index(letter)
            if keymacropressed[keyindex] == False:
                print('pressing: '+keys[keyindex])
                keyboard.press(keys[keyindex])
                keymacropressed[keyindex] = True
            else:
                print('releasing: '+keys[keyindex])
                keyboard.release(keys[keyindex])
                keymacropressed[keyindex] = False


###########-LOOP-###########
print('#####-MADE-BY-UKII-#####')
loadfiles()
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
