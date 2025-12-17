# FlyEarth-07

This GitHib repo enables a BBC micro:bit (mbit) to be used to simulate the experience of flying in Google Earth Web. The mbit senses pitch and roll in its accelerometers, and sends keystrokes via bluetooth to a loptop running Google Earth in a browser. Video at xixx. Code is written in blocks in MakeCode.

The BLE-HID (Bluetooth Low Energy - Human Interface Device) Extention by Bill Siever is used. Thank you Bill!

The purpose of this project is not only to enable young people to explore the world, it is also to provide an example of how to develop good engineering skills for making things work with teamwork. It's more fun and less work. The principles of systems engineering are encapsulated in Deming's Plan-Do-Check-Act. Learn how to use it and everbody will have a much better day.

## Installation Guide

If you are new to mbit, please familiarize yourself at makecode.microbit.org and make sure you can download to and run projects first.

### Required Hardware

1. BBC MicroBit v2 recommended, with battery box and usb cable
2. PC with browser and internet connection. Tested with Windows 11 on an i7. Let me know how Mac and Chromebook work.
3. Google Earth Web, not the Earth Pro or mobile apps. they may not recognize keystrokes or render 3D buildings.

### Installation Steps

In these steps '->' indicates the expected result.

#### In a browser on a laptop:

1. Open https://makecode.microbit.org/ -> Make code opens
2. Click the 'Import' button at center right -> Dialog opens
3. Click button at middle top 'Import URL ...' -> Dialog updates
4. Enter this url as 'URL of the project' https://github.com/4-R-Forum/flyearth-07
5. Click 'Go Ahead!' -> Project opens showing 'on start' blocks
6. Connect mbit to PC with USB cable -> mbit lights come on
7. Click 'Download' button at bottom left -> Project downloads
    - if download fails, remove usb cable, reconnect and try again
8. Leds indicate roll and pitch, when you tilt the mbit
9. Remove the usb cable -> lights go out

#### Connect PC bluetooth to MicroBit

1. Open Windows Control Panel
2. Select Bluetooth and Devices
3. Make sure Bluetooth is turned on at top
4. Press 'Add Device' button -> dialog opens
    - Click 'Bluetooth'
5.  - Click 'show all devices'
6. When connected BBC micro:bit shows as connected
7. If Bluetooth connection fails, go to the TroubleShootingGuide

That's the trickiest part of setup. Once you are connected you laptop will remember BBC Microbit and connect again easily. If not, repeat all the steps.

### Open Google Earth in a browser

1. Use Chrome or Edge, both work equally well
2. Standard (free) Google Earth is all you needh/answer/7365484
    - Use the web version, to fly with [keystrokes](https://developers.google.com/maps/documentation/earth/use-keyboard-shortcuts)
    - Google Earth Pro App is not supported
3. Login to Google is optional
4. Type https://earth.google.com/ into the address bar at top -> Google Earth opens
5. Click 'Explore Earth at top right. -> View of the globe appears

### Navigate to where you want to go

Let's start with the the Pyramids.

1. Type "Great Pyrmamid of Giza" into the searchbox at top left and press Enter -> flies you there
2. Press letter "O" then any other key to stop rotating -> view changes from 2D to 3D and stops
3. Press and hold Shift-DownArrow until horizon appears
4. Press "?" -> Keyboard shortcut dialog is  displayed, press x at top right to closeit
5. Now you are ready to fly

## **Fly Earth!**

1. Turn the micro_bit on and hold it level -> center led lights
2. Tilt it forward -> second row led lights, you fly forward
3. Tilt it left -> second column led lithts, you fly left
4. Tilt more left -> left column led lights, you turn left
5. Tilt more forward -> top row center led lights, you go up
6. Tilt other directions -> opposite of above
7. Hold level -> you stop.

## Release Notes
1. First release of FlyEarth-07. In work 12/15/2025