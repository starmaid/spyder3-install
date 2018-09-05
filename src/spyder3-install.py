# -*- coding: utf-8 -*-
"""
Nicholas Masso
8-31-2018
nicholas.masso.14@gmail.com
nmasso@purdue.edu

This code is run from the python CLE to:
    -upgrade pip
    -install spyder
    -create a desktop shortcut to spyder
on any operating system.

This takes the extra complications of Anaconda
out of the equation when setting up an IDE
"""
import sys
import os
import path
    
def installs(pypath):
    os.system(pypath+' -m pip install --upgrade pip')
    os.system(pypath+' -m pip install spyder --no-warn-script-location')
    #no warnings for adding spyder to PATH, i dont think thats really needed

here = path.abspath(path.dirname(__file__))

if sys.platform.startswith('win32') or  sys.platform.startswith('cygwin'):
    #windows
    
    #first, use the PATH reference to python.exe on windows cmd
    installs('py')
    
    #these are specific packages to create shortcuts on windows 7+
    os.system('py -m pip install winshell')
    os.system('py -m pip install pypiwin32')
    import winshell
    #winshell imports pypiwin32, so theres no need to import it
    
    #this is the directory of your python.exe file
    python_dir = sys.executable
    #pip installs spyder in a subfolder in that location
    spyder_dir = python_dir.replace('python.exe','Scripts\spyder3.exe')
    
    #uncomment these if the shortcut isnt showing up
    #print(sys.executable)    
    #print(spyder_dir)
    
    #this creates the shortcut
    #TODO: use the spyder logo as the icon
    link_filepath = os.path.join(winshell.desktop(), "Spyder 3.lnk")
    with winshell.shortcut(link_filepath) as link:
        link.path = spyder_dir
        link.description = "Shortcut to Spyder IDE"
        link.icon = here+"/spyder.ico"
elif sys.platform.startswith('darwin'):
    #mac osX
    installs('python3')
    
    #TODO: follow instructions at
    # https://www.sethvargo.com/replace-icons-osx/
    #to make the shortcut file...spyder.icns is in /src
    
elif sys.platform.startswith('linux'):
    #Linux
    installs('python3')
else:
    #this is for other unix-based systems
    installs()

