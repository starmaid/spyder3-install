"""
This code is run from the python CLE to:
    -upgrade pip
    -install spyder
    -create a desktop shortcut to spyder
on any operating system.

This takes the extra complications of Anaconda
out of the equation when setting up an IDE

Usage:
    python3 spy....
"""
import sys
import os

# Update usage
# Rename installs and add docstring
    
def installs(pypath):
    os.system( pypath + ' -m pip install --upgrade pip' )
    os.system( pypath + ' -m pip install spyder --no-warn-script-location' )
    # No warnings for adding spyder to PATH, i dont think thats really needed

#find the path that we are installing to
here = os.path.abspath(os.path.dirname( __file__ ))

if sys.platform.startswith( 'win32' ) or sys.platform.startswith( 'cygwin' ):
    # For use on Windows OS machines
    
    # First, use the PATH reference to python.exe on windows cmd
    installs( 'py' )
    
    # These are specific packages to create shortcuts on windows 7+
    os.system( 'py -m pip install winshell' )
    os.system( 'py -m pip install pypiwin32' )
    
    import winshell
    # Winshell imports pypiwin32, so theres no need to import it
    
    # This is the directory of your python.exe file
    python_dir = sys.executable
    
    # Pip installs spyder in a subfolder in that location
    spyder_dir = python_dir.replace( 'python.exe' , 'Scripts\spyder3.exe' )
    
    # This segment creates the shortcut
    link_filepath = os.path.join( winshell.desktop() , "Spyder 3.lnk" )
    with winshell.shortcut(link_filepath) as link:
        # Path to the program
        link.path = spyder_dir
        # Description
        link.description = "Shortcut to Spyder IDE"
        # Dhere the icon file is
        link.icon_location = here + "/spyder.ico" , 0

elif sys.platform.startswith( 'darwin' ):
    # For use on Mac osX
    installs('python3')
    
    #TODO: follow instructions at
    # https://www.sethvargo.com/replace-icons-osx/
    #to make the shortcut file...spyder.icns is in /src
    
elif sys.platform.startswith('linux'):
    # Linux
    installs('python3')
else:
    # This is for other unix-based systems
    print('Sorry, this script does not support your OS.')
    print('Consider opening it in a text editor and following the steps')
    os.system('read -p "Press ENTER to continue"')
    #installs()

