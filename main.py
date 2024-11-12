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

keyboard.start_keyboard_service()
keyboard.set_events_per_second(1)