def turnLeft():
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.RIGHT),
        False)
def goBack():
    keyboard.send_string(keyboard.keys(keyboard._Key.DOWN))
# determine keys to send based on input text parameter
def makeMove(text: str):
    global tm, lm
    # if param is gF, send sh-up
    # else turn hold off and call appropriate move to send keys
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
# For unit test of a single move

def on_logo_long_pressed():
    loadKML()
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def goForward():
    keyboard.send_string(keyboard.keys(keyboard._Key.UP))
def test3():
    # PgDown USB hex 4E
    keyboard.send_string(keyboard.raw_scancode(78))
# using current pitch set leds and make move based on thresholds
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
def test1():
    # result
    # kd shift
    # kd downarrow
    # ku shift
    # ky downarrow
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.raw_scancode(81),
        True)
# For debugging keystrokes
# Pess B to repeat key
# Press A for next key
def waitA(move: str):
    while not (input.button_is_pressed(Button.A)):
        if input.button_is_pressed(Button.B):
            keyboard.release_keys()
            makeMove(move)
        continue
def test4():
    # PgDown USB hex 4E
    keyboard.send_string(keyboard.raw_scancode(75))
def loadKML():
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.CONTROL) + "i",
        False)
# kd backxpace
# ku backspace
# kd down arrow
# ky down arrow
def test2():
    # shift
    keyboard.send_string(keyboard.raw_scancode(42))
    # PgDown PS/2
    keyboard.send_string(keyboard.raw_scancode(81))
def lookUp():
    keyboard.send_simultaneous_keys("" + keyboard.modifiers(keyboard._Modifier.SHIFT) + keyboard.keys(keyboard._Key.DOWN),
        False)
def goRight():
    keyboard.send_string(keyboard.keys(keyboard._Key.RIGHT))
# pitch takes priority else update leds and make move based on thresholds
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
    # 0x4B in USB HID standard
    keyboard.send_string(keyboard.raw_scancode(75))
# For debugging keystrokes

def on_logo_pressed():
    basic.show_string("gF")
    waitA("gF")
    basic.show_string("gB")
    waitA("gB")
    basic.show_string("gU")
    waitA("gU")
    basic.show_string("gD")
    waitA("gD")
    basic.show_string("gL")
    waitA("gL")
    basic.show_string("tL")
    waitA("tL")
    basic.show_string("gR")
    waitA("gR")
    basic.show_string("tR")
    waitA("tR")
    basic.show_string("lU")
    waitA("lU")
    basic.show_string("lD")
    waitA("lD")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def goUp():
    # 0x4E in USB HID standard
    # shows as Ox51 PageDown in KbKeyInfo
    keyboard.send_string(keyboard.raw_scancode(78))
# - Executes when mbit powered on.
# - t1 & t2 are thresholds in degrees for both pitch and roll
# - keyboard service starts with 1 key/sec
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
basic.pause(1000)
loadKML()
# main loop. set vars r and p, call doRoll

def on_forever():
    global r, p
    r = input.rotation(Rotation.ROLL)
    p = input.rotation(Rotation.PITCH)
    doRoll()
basic.forever(on_forever)
