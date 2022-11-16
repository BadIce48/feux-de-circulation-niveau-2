feux_rouge2 = False
pieton = False
def clignoter_led_orange_pieton():
    for index in range(25):
        pins.digital_write_pin(DigitalPin.P8, 1)
        basic.pause(200)
        pins.digital_write_pin(DigitalPin.P8, 0)
        basic.pause(200)
def feux_rouge():
    global feux_rouge2
    pins.digital_write_pin(DigitalPin.P2, 1)
    feux_rouge2 = True
def eteindre_feux_jaune():
    pins.digital_write_pin(DigitalPin.P1, 0)
def eteindre_feux_rouge():
    global feux_rouge2
    pins.digital_write_pin(DigitalPin.P2, 0)
    feux_rouge2 = False
def feux_jaune():
    pins.digital_write_pin(DigitalPin.P1, 1)

def on_button_pressed_a():
    global pieton
    if feux_rouge2 == True:
        pieton = True
        basic.pause(10000)
        pieton = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def Feux_vert():
    pins.digital_write_pin(DigitalPin.P0, 1)
def eteindre_led_blanche_pieton():
    pins.digital_write_pin(DigitalPin.P16, 0)
def eteindre_feux_vert():
    pins.digital_write_pin(DigitalPin.P0, 0)
def led_orange_pieton():
    pins.digital_write_pin(DigitalPin.P8, 1)
def led_blanche_pieton():
    pins.digital_write_pin(DigitalPin.P16, 1)
def eteindre_led_orange_pieton():
    pins.digital_write_pin(DigitalPin.P8, 0)

def on_forever():
    while pieton == False:
        Feux_vert()
        basic.pause(5000)
        eteindre_feux_vert()
        feux_jaune()
        basic.pause(2000)
        eteindre_feux_jaune()
        feux_rouge()
        basic.pause(5000)
        eteindre_feux_rouge()
    if pieton == True and feux_rouge2 == True:
        feux_rouge()
        led_blanche_pieton()
        basic.pause(5000)
        clignoter_led_orange_pieton()
        eteindre_led_orange_pieton()
        eteindre_led_blanche_pieton()
        eteindre_feux_rouge()
basic.forever(on_forever)
