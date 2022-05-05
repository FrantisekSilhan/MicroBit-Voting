radio.set_group(69)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)

def on_button_pressed_a():
    btmc = "KAZDA JE DOBRY UCITEL"
    for i in range(len(btmc)):
        print(btmc.char_code_at(i)-64)
        radio.send_value("vote", btmc.char_code_at(i)-64)
        pause(300)
input.on_button_pressed(Button.A, on_button_pressed_a)
