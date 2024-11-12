def on_logo_pressed():
    basic.show_string("fw")
    keyboard.send_string(keyboard.keys(keyboard._Key.UP))
    basic.show_string("bk")
    keyboard.send_string(keyboard.keys(keyboard._Key.DOWN))
    basic.show_string("up")
    keyboard.send_string(keyboard.raw_scancode(91))
    basic.show_string("dn")
    keyboard.send_string(keyboard.raw_scancode(97))
    basic.show_string("gL")
    keyboard.send_string(keyboard.keys(keyboard._Key.LEFT))
    basic.show_string("tL")
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.RIGHT),
        False)
    basic.show_string("gR")
    keyboard.send_string(keyboard.keys(keyboard._Key.RIGHT))
    basic.show_string("Tr")
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.LEFT),
        False)
    basic.show_string("lu")
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.DOWN),
        False)
    basic.show_string("ld")
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.UP),
        False)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

t1 = 20
t2 = 40
r = 0
p = 0
keyboard.start_keyboard_service()
keyboard.set_events_per_second(1)

def on_forever():
    global r, p
    r = input.rotation(Rotation.ROLL)
    p = input.rotation(Rotation.PITCH)
    doRoll()
basic.forever(on_forever)

def doRoll():
    if r > 0 - t1 and r < t1:
        doPitch()
    elif r < 0 - t2:
        basic.show_leds("""
    . . . . .
    . . . . .
    # . . . .
    . . . . .
    . . . . .
    """)
    #turnLeft
    elif r < 0 - t1:
        basic.show_leds("""
        . . . . .
        . . . . .
        . # . . .
        . . . . .
        . . . . .
        """)
        #gotLeft
    elif r > t2:
        basic.show_leds("""
        . . . . .
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        """)
        #turnRight
    else:
        basic.show_leds("""
        . . . . .
        . . . . .
        . . . # .
        . . . . .
        . . . . .
        """)
        #goRight

def doPitch():
    if p > 0 - t1 and p < t1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        # goDown
    elif p < 0 - t2:
        basic.show_leds("""
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        #goForward
    elif p < 0 - t1:
        basic.show_leds("""
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif p > t2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            """)
    # goUp
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            """)
        #goBack
