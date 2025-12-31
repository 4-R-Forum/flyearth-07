# FlyEarth-07 TroubleShooting Guide

## Connecting Bluetooth BLE

Microbit uses Bluetooth Low Energy (BLE)  which saves energy by attemtpting to connect when it is turned on, and limiting time it attempts to connect.  

1. If connection fails
    - Close the connecting dialog if it is open
    - Make sure your batteries are fully charged, weak batteries may cause BLE to connect.
    - Make sure you have 'show all devices' selected in the Bluetooth Settig
    - turn micro:bit off and wait a few seconds
    - turn micro:bit on again, BLE will try again
    - Click 'Add device' button in Bluetooth & devices window
    - make sure 'Show all devices' is clicked
    - ignore 'Unknown' devices
2. You may need to be patient and try several times.


## Human Interface Device (HID) keyboard scancodes

Bill Siever's microbit-pxt-blehid micro:bit extension and its documentation (RMB Help in MakeCode) are excellent. It makes most keys simple to send with sendkeys(), and provides a means of sending all keys with rawscancode().

Non letter keys such as PageUp and PageDown are not simple because standards for keyboards, and the numeric codes that represent them, have changed over the years. Unravelling this for your computer keyboard may be complicated, as it was for me.

There are functions in the project code to help with identifying the correct rawscancodes. Post an issue in GitHub and I will help you resolve the issue.