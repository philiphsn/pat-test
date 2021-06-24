music.play_melody("C5 B F G F B D C ", 120)

def on_forever():
    pass
basic.forever(on_forever)

basic.show_arrow(ArrowNames.NORTH)
while True:
    bluetooth.start_button_service()
    led.plot_bar_graph(0, 0)
bluetooth.start_io_pin_service()
if True:
    music.play_tone(Note.C, music.beat())
else:
    serial.write_value("x", 0)
    led.toggle(0, 0)
basic.showleds()
basic.show_leds("""
. . . . .
. . . . .
. . # . .
. . . . .
. . . . .
""")