feux_rouge = False
pieton = False
décompte = 0
def clignoter_led_orange_pieton():
    for index in range(25):
        pins.digital_write_pin(DigitalPin.P8, 1)
        basic.pause(200)
        pins.digital_write_pin(DigitalPin.P8, 0)
        basic.pause(200)
def eteindre_feux_jaune():
    pins.digital_write_pin(DigitalPin.P1, 0)
def eteindre_feux_rouge():
    global feux_rouge
    pins.digital_write_pin(DigitalPin.P2, 0)
    feux_rouge = False
def feux_jaune():
    pins.digital_write_pin(DigitalPin.P1, 1)

def on_button_pressed_a():
    global pieton
    pieton = True
    basic.pause(20000)
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
def feux_rouge2():
    global feux_rouge
    pins.digital_write_pin(DigitalPin.P2, 1)
    feux_rouge = True
def led_blanche_pieton():
    pins.digital_write_pin(DigitalPin.P16, 1)
def eteindre_led_orange_pieton():
    pins.digital_write_pin(DigitalPin.P8, 0)

def on_forever():
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
    if pieton == True:
        feux_rouge2()
        eteindre_led_orange_pieton()
        led_blanche_pieton()
        basic.pause(5000)
        eteindre_led_orange_pieton()
        clignoter_led_orange_pieton()
        eteindre_led_blanche_pieton()
        eteindre_feux_rouge()
basic.forever(on_forever)

def on_forever2():
    global décompte
    if pieton == True:
        basic.pause(5000)
        décompte = 30
        if feux_rouge == True:
            for index2 in range(10):
                basic.show_number(décompte)
                basic.pause(500)
                décompte += -1
                basic.pause(500)
    basic.clear_screen()
basic.forever(on_forever2)
