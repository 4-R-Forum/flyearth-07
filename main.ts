function turnLeft () {
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.right), false)
}
function goBack () {
    keyboard.sendString(keyboard.keys(keyboard._Key.down))
}
function makeMove (text: string) {
    if (text == "gF") {
        tm = text
        if (lm != tm) {
            keyboard.sendSimultaneousKeys("" + keyboard.keys(keyboard._Key.up), true)
        }
        lm = tm
    } else {
        keyboard.releaseKeys()
        if (text == "gB") {
            goBack()
        } else if (text == "gU") {
            goUp()
        } else if (text == "gD") {
            goDown()
        } else if (text == "gR") {
            goRight()
        } else if (text == "tR") {
            turnRight()
        } else if (text == "gL") {
            goLeft()
        } else if (text == "tL") {
            turnLeft()
        } else if (text == "lU") {
            lookUp()
        } else if (text == "lD") {
            lookDown()
        }
        lm = text
    }
}
function goForward () {
    keyboard.sendString(keyboard.keys(keyboard._Key.up))
}
function doPitch () {
    if (p > 0 - t1 && p < t1) {
        // hover, no move
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        makeMove("")
    } else if (p < 0 - t2) {
        // goDown
        basic.showLeds(`
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        makeMove("gD")
    } else if (p < 0 - t1) {
        // goForward
        basic.showLeds(`
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            `)
        makeMove("gF")
    } else if (p > t2) {
        // goUp
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `)
        makeMove("gU")
    } else if (p > t1) {
        // goUp
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            `)
        makeMove("gU")
    } else {
        makeMove("")
    }
}
function waitA () {
    while (!(input.buttonIsPressed(Button.A))) {
        continue;
    }
}
function lookUp () {
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.down), false)
}
function goRight () {
    keyboard.sendString(keyboard.keys(keyboard._Key.right))
}
function doRoll () {
    if (r > 0 - t1 && r < t1) {
        // no roll, do doPitch
        doPitch()
    } else if (r < 0 - t2) {
        // turnLeft
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
        makeMove("tL")
    } else if (r < 0 - t1) {
        // goLeft
        basic.showLeds(`
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            `)
        makeMove("gL")
    } else if (r > t2) {
        // turnRight
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            `)
        makeMove("tR")
    } else {
        // goRight
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . # .
            . . . . .
            . . . . .
            `)
        makeMove("gR")
    }
}
function goLeft () {
    keyboard.sendString(keyboard.keys(keyboard._Key.left))
}
function turnRight () {
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.left), false)
}
function lookDown () {
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.up), false)
}
function goDown () {
    keyboard.sendString(keyboard.rawScancode(97))
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("fw")
    keyboard.sendString(keyboard.keys(keyboard._Key.up))
    waitA()
    basic.showString("bk")
    keyboard.sendString(keyboard.keys(keyboard._Key.down))
    waitA()
    basic.showString("up")
    keyboard.sendString(keyboard.rawScancode(91))
    waitA()
    basic.showString("dn")
    keyboard.sendString(keyboard.rawScancode(97))
    waitA()
    basic.showString("gL")
    keyboard.sendString(keyboard.keys(keyboard._Key.left))
    waitA()
    basic.showString("tL")
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.right), false)
    basic.showString("gR")
    waitA()
    keyboard.sendString(keyboard.keys(keyboard._Key.right))
    basic.showString("Tr")
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.left), false)
    basic.showString("lu")
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.down), false)
    waitA()
    basic.showString("ld")
    keyboard.sendSimultaneousKeys("" + keyboard.modifiers(keyboard._Modifier.shift) + keyboard.keys(keyboard._Key.up), false)
})
function goUp () {
    keyboard.sendString(keyboard.rawScancode(91))
}
let r = 0
let p = 0
let lm = ""
let tm = ""
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
