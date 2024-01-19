# Host status

This is a simple script I use on my devices that checks to see if devices I use on my network are up and running or are down and prints which ones are up and down in either green or red using ANSI Escape color sequences. 

Overall, this code is an easy way to see what key components of my network are up and running.

# Libraries Used

Modules: 

 - Socket

The socket module as well as socket API in short is used to send messages across the network.  More detailed information on this module you can found [here](https://docs.python.org/3/library/socket.html).



# Triggering this Code

For me personally I am a primarily Mac user so I can take advantage of shortcuts (with the addition of support of AppleScript). 

The Apple Script I use via Shortcuts is: 

    tell application "Terminal"
	    do script "python3 /Users/m1macmini/Desktop/Scripts/up.py"
	    delay 10
	end tell

I use a second Apple script to quit Terminal within the same shortcut.  That script is: 

    tell applicaiton "Terminal"
	    quit
	end tell

I can quickly trigger it from the desktop widget (feature of Sonoma), within the menu bar or other automations. 

