let pieton = false
function clignoter_led_orange_pieton () {
    for (let index = 0; index < 25; index++) {
        pins.digitalWritePin(DigitalPin.P8, 1)
        basic.pause(200)
        pins.digitalWritePin(DigitalPin.P8, 0)
        basic.pause(200)
    }
}
function feux_rouge () {
    pins.digitalWritePin(DigitalPin.P2, 1)
}
function eteindre_feux_jaune () {
    pins.digitalWritePin(DigitalPin.P1, 0)
}
function eteindre_feux_rouge () {
    pins.digitalWritePin(DigitalPin.P2, 0)
}
function feux_jaune () {
    pins.digitalWritePin(DigitalPin.P1, 1)
}
input.onButtonPressed(Button.A, function () {
    pieton = true
    basic.pause(10000)
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
function led_blanche_pieton () {
    pins.digitalWritePin(DigitalPin.P16, 1)
}
function eteindre_led_orange_pieton () {
    pins.digitalWritePin(DigitalPin.P8, 0)
}
basic.forever(function () {
    while (pieton == false) {
        Feux_vert()
        basic.pause(5000)
        eteindre_feux_vert()
        feux_jaune()
        basic.pause(2000)
        eteindre_feux_jaune()
        feux_rouge()
        basic.pause(5000)
        eteindre_feux_rouge()
    }
    if (pieton == true) {
        led_blanche_pieton()
        basic.pause(5000)
        clignoter_led_orange_pieton()
        eteindre_led_orange_pieton()
    }
})
