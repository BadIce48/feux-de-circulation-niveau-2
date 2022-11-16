let feux_rouge = false
let pieton = false
let décompte = 0
function clignoter_led_orange_pieton () {
    for (let index = 0; index < 25; index++) {
        pins.digitalWritePin(DigitalPin.P8, 1)
        basic.pause(200)
        pins.digitalWritePin(DigitalPin.P8, 0)
        basic.pause(200)
    }
}
function eteindre_feux_jaune () {
    pins.digitalWritePin(DigitalPin.P1, 0)
}
function eteindre_feux_rouge () {
    pins.digitalWritePin(DigitalPin.P2, 0)
    feux_rouge = false
}
function feux_jaune () {
    pins.digitalWritePin(DigitalPin.P1, 1)
}
input.onButtonPressed(Button.A, function () {
    pieton = true
    basic.pause(20000)
    pieton = false
})
function Feux_vert () {
    pins.digitalWritePin(DigitalPin.P0, 1)
}
function eteindre_led_blanche_pieton () {
    pins.digitalWritePin(DigitalPin.P16, 0)
}
function eteindre_feux_vert () {
    pins.digitalWritePin(DigitalPin.P0, 0)
}
function led_orange_pieton () {
    pins.digitalWritePin(DigitalPin.P8, 1)
}
function feux_rouge2 () {
    pins.digitalWritePin(DigitalPin.P2, 1)
    feux_rouge = true
}
function led_blanche_pieton () {
    pins.digitalWritePin(DigitalPin.P16, 1)
}
function eteindre_led_orange_pieton () {
    pins.digitalWritePin(DigitalPin.P8, 0)
}
basic.forever(function () {
    led_orange_pieton()
    Feux_vert()
    basic.pause(5000)
    eteindre_feux_vert()
    feux_jaune()
    basic.pause(2000)
    eteindre_feux_jaune()
    feux_rouge2()
    basic.pause(5000)
    eteindre_feux_rouge()
    if (pieton == true) {
        feux_rouge2()
        eteindre_led_orange_pieton()
        led_blanche_pieton()
        basic.pause(5000)
        eteindre_led_orange_pieton()
        clignoter_led_orange_pieton()
        eteindre_led_blanche_pieton()
        eteindre_feux_rouge()
    }
})
basic.forever(function () {
    if (pieton == true) {
        décompte = 30
        basic.showNumber(décompte)
        décompte += -1
    }
    if (décompte == 30) {
        basic.clearScreen()
    }
})
