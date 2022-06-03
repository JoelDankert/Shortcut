# Shortcut
Shortcut is a python project for creating shortcuts to quickly type text. It can also be used to create macros.

## Installation
pip installs:
```bash
pip install keyboard
pip install mouse
```

Install the shortcut.py file from the shortcut repository and run it

## Usage

### Adding files
To add a file, create one or multiple '.short' files in the same folder of your application to start creating shortcuts.

'.short' files are built like this:

```bash
#lines starting with '#' will be ignored.
text or macro (create text, create macro)
corresponding shortcut (create shortcut)
```
A '.short' file can contain as many shortcuts as you want, as long as you seperate them using a new line.

### Create text
To create text, simply type the text you want in one line, use a '%' to type a new line. You can also use '\*' to wait 0.1 seconds before continuing.

### Create shortcut
To create a shortcut, type the keystrokes in a new line under the text or macro, each keystroke is represented by a pair of two letters.  
'a ', 'b ', 'c ', ...  
are used for letters from the default english alphabet. Note that after keys, which only use one letter, a whitespace ('space') follows.  
Other Keys like tab, alt, shift, control and windows are represented using  
'ta', 'al', 'sh', 'co', 'wi'.  
All supported letters can be found in the 'keys' list with the corresponding two letter names in the 'keystell' list.

Example for pressing 'e','m','tab' to replace it with your email:
```bash
#this is an example for a '.short' file
your.email@provider.com
e m ta
```

### Create macro
to create macros use an '&' in front of your line. use the same two letter keycodes as in 'Create shortcut'. To press a key, type the keycode, then type the keycode again to release a key.  
For example, ctrl + z would look like this:

```bash
&coz z co
shortcut
```
'&' indicate macro  
'co' press control  
'z ' press z  
'z ' release z  
'co' release control
