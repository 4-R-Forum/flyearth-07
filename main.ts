// goRight
function doPitch () {
    if (p > 0 - t1 && p < t1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    } else if (p < 0 - t2) {
        // goDown
        basic.showLeds(`
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (p < 0 - t1) {
        // goForward
        basic.showLeds(`
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (p > t2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `)
    } else {
        // goUp
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            `)
    }
}
function doRoll () {
    if (r > 0 - t1 && r < t1) {
        doPitch()
    } else if (r < 0 - t2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
    } else if (r < 0 - t1) {
        // turnLeft
        basic.showLeds(`
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            `)
    } else if (r > t2) {
        // gotLeft
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            `)
    } else {
        // turnRight
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . # .
            . . . . .
            . . . . .
            `)
    }
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("fw")
    keyboard.sendString(keyboard.keys(keyboard._Key.up))
    basic.showString("bk")
    keyboard.sendString(keyboard.keys(keyboard._Key.down))
    basic.showString("up")
    keyboard.sendString(keyboard.rawScancode(91))
    basic.showString("dn")
    keyboard.sendString(keyboard.rawScancode(97))
    basic.showString("gL")
    keyboard.sendString(keyboard.keys(keyboard._Key.left))
    basic.showString("tL")
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.right), false)
    basic.showString("gR")
    keyboard.sendString(keyboard.keys(keyboard._Key.right))
    basic.showString("Tr")
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.left), false)
    basic.showString("lu")
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.down), false)
    basic.showString("ld")
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.up), false)
})
let r = 0
let p = 0
let t2 = 0
let t1 = 0
t1 = 20
t2 = 40
keyboard.startKeyboardService()
keyboard.setEventsPerSecond(1)
basic.forever(function () {
    r = input.rotation(Rotation.Roll)
    p = input.rotation(Rotation.Pitch)
    doRoll()
})
