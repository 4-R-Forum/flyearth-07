def turnLeft():
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.RIGHT),
        False)
def goBack():
    keyboard.send_string(keyboard.keys(keyboard._Key.DOWN))
def makeMove(text: str):
    global tm, lm
    if text == "gF":
        tm = text
        if lm != tm:
            keyboard.send_simultaneous_keys("" + keyboard.keys(keyboard._Key.UP), True)
        lm = tm
    else:
        keyboard.release_keys()
        if text == "gB":
            goBack()
        elif text == "gU":
            goUp()
        elif text == "gD":
            goDown()
        elif text == "gR":
            goRight()
        elif text == "tR":
            turnRight()
        elif text == "gL":
            goLeft()
        elif text == "tL":
            turnLeft()
        elif text == "lU":
            lookUp()
        elif text == "lD":
            lookDown()
        lm = text
def goForward():
    keyboard.send_string(keyboard.keys(keyboard._Key.UP))
def doPitch():
    if p > 0 - t1 and p < t1:
        # hover, no move
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        makeMove("")
    elif p < 0 - t2:
        # goDown
        basic.show_leds("""
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        makeMove("gD")
    elif p < 0 - t1:
        # goForward
        basic.show_leds("""
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            """)
        makeMove("gF")
    elif p > t2:
        # goUp
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            """)
        makeMove("gU")
    elif p > t1:
        # goUp
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            """)
        makeMove("gU")
    else:
        makeMove("")
def waitA():
    while not (input.button_is_pressed(Button.A)):
        continue
def lookUp():
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.DOWN),
        False)
def goRight():
    keyboard.send_string(keyboard.keys(keyboard._Key.RIGHT))
def doRoll():
    if r > 0 - t1 and r < t1:
        # no roll, do doPitch
        doPitch()
    elif r < 0 - t2:
        # turnLeft
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
        makeMove("tL")
    elif r < 0 - t1:
        # goLeft
        basic.show_leds("""
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            """)
        makeMove("gL")
    elif r > t2:
        # turnRight
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            """)
        makeMove("tR")
    else:
        # goRight
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . # .
            . . . . .
            . . . . .
            """)
        makeMove("gR")
def goLeft():
    keyboard.send_string(keyboard.keys(keyboard._Key.LEFT))
def turnRight():
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.LEFT),
        False)
def lookDown():
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.UP),
        False)
def goDown():
    keyboard.send_string(keyboard.raw_scancode(97))

def on_logo_pressed():
    basic.show_string("fw")
    keyboard.send_string(keyboard.keys(keyboard._Key.UP))
    waitA()
    basic.show_string("bk")
    keyboard.send_string(keyboard.keys(keyboard._Key.DOWN))
    waitA()
    basic.show_string("up")
    keyboard.send_string(keyboard.raw_scancode(91))
    waitA()
    basic.show_string("dn")
    keyboard.send_string(keyboard.raw_scancode(97))
    waitA()
    basic.show_string("gL")
    keyboard.send_string(keyboard.keys(keyboard._Key.LEFT))
    waitA()
    basic.show_string("tL")
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.RIGHT),
        False)
    basic.show_string("gR")
    waitA()
    keyboard.send_string(keyboard.keys(keyboard._Key.RIGHT))
    basic.show_string("Tr")
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.LEFT),
        False)
    basic.show_string("lu")
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.DOWN),
        False)
    waitA()
    basic.show_string("ld")
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.UP),
        False)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def goUp():
    keyboard.send_string(keyboard.raw_scancode(91))
r = 0
p = 0
lm = ""
tm = ""
t2 = 0
t1 = 0
t1 = 20
t2 = 40
keyboard.start_keyboard_service()
keyboard.set_events_per_second(1)

def on_forever():
    global r, p
    r = input.rotation(Rotation.ROLL)
    p = -21
    doRoll()
basic.forever(on_forever)
