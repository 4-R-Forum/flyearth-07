# FlyEarh-07 User Guide

## Setup

Follow instructions in Installation-Guide

## How to Fly

### Open Google Earth in a browser


1. Use Chrome or Edge, both work equally well
2. Standard (free) Google Earth is all you need
    - Use the web version, to fly with [keystrokes](https://developers.google.com/maps/documentation/earth/use-keyboard-shortcuts)
    - Google Earth Pro App is not supported
3. Login to Google is optional
4. Type https://earth.google.com/ into the address bar at top -> Google Earth opens
5. Click 'Explore Earth at top right. -> View of the globe appears


## **Fly Earth!**

1. Turn the micro:bit on and hold it level -> checkerboard pattern displays
2. File dialog opens, select local KML file from Documentation folder in the repo
    - press Cancel to type in starting point, continue in Optional, below
3. Earth flies you to the selected location
4. Hold micro:bit level -> center led light shows
5. Tilt it forward -> second row led lights, you fly forward
6. Tilt it left -> second column led lithts, you fly left
7. Tilt more left -> left column led lights, you turn left
8. Tilt more forward -> top row center led lights, you go up
9. Tilt other directions -> opposite of above
10. Hold level -> you stop.
11. Turn micro_bit off

### Optional, type in starting point

Let's start at the the Pyramids.

1. Type https://earth.google.com/ into the address bar at top -> Google Earth opens
2. Click 'Explore Earth at top right. -> View of the globe appears
3. Type "Great Pyramid of Giza" into the searchbox at top left  and press Enter -> flies you there
4. Press letter "O", then any other key to stop rotating -> view changes from 2D to 3D and stops
5. Press and hold Shift-DownArrow until horizon appears
6. Press "?" -> Keyboard shortcut dialog is  displayed, press x at top right to closeit
7. Now you are ready to fly

## Creating KML files

1. Use the optional step above to find your starting point
2. In the File menu at top left, Create a new Map -> Name Untitled appears above File menu at top
3. Add a Placemark, give it a name, such as 'Start' -> Placemark shows in Map at left
4. Double click Placemark at left -> Dialog opens at right
5. Click Edit button at bottom left of Dialog -> Details appear in dialog
6. Scroll down in dialog and click button 'Capture this view' -> Details are updated
7. In the File menu at top left, Export as KML File -> File is dowloaded to your browser
8. If you are loggged into your Google Account, the file should also be in your Google Drive.
9. Now you need to edit your KML file, you can do this in any text editor including Notepad.
    - Find the <Placemark id="123ABC..."> element.
    - Nested within it is the <LookAt> element, cut and paste it to just above and outside the Placemark element.
    - Save the edited KML file.
10. Use the new KML file to start flying when the File dialog opens.
 