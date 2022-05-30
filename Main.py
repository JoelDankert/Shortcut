import keyboard
import time

word = []
shortcut = []

#accounts
word.extend(['joel.dankert@gmail.com','+4917660186268','Ukii#3647','Ukii','xXUkiiXx'])
shortcut.extend(['e m # ','t e l # ','d c # ','s t e a m # ','e p i c # '])

#abkürzungen
word.extend(['sorry','nice try','good luck, have fun!','my bad','thank you','no problem','good job'])
shortcut.extend(['s r y # ','n t # ','g l h f # ','m b # ','t h x # ','n p # ','g j # '])

#addresses
word.extend(['Aschenreutestraße 1, 78591 Durchhausen','Sallancher Str. 5, 78549 Spaichingen','In d. Breite 21, 78591 Durchhausen'])
shortcut.extend(['a d . h o m e # ','a d . s c h o o l # ','a d . f a d w # '])

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','ä','ö','ü','ß','1','2','3','4','5','6','7','8','9','0','.',',','#','space','+','-','tab','shift','ctrl','alt']
keystell = ['a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ', 'n ', 'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 'y ','z ','ae','oe','ue','ss','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','0 ','. ',', ','# ','  ','+ ','- ','ta','sh','co','al']
keyremove = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0]


#                                                                                                                                       
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
