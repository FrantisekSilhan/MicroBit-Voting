radio.set_group(69)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)

enabled = 0
serial_list = [control.device_serial_number()]
choice_list = [0]

radio.on_received_value(on_received_value)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, reset)

def on_received_value(name, value):
    global serial_list, choice_list
    if enabled == 1:
        remote_serial = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        if name == "vote":
            if remote_serial in serial_list:
                choice_list[serial_list.index(remote_serial)] = value
            else:
                choice_list.append(value)
                serial_list.append(remote_serial)
            print("Nový hlas: "+String.from_char_code(64+value)+" od "+remote_serial)
            music.play_tone(Note.C, 500)

def on_button_pressed_a():
    global enabled
    if enabled == 0: enabled = 1
    else: enabled = 0
    radio.send_value("enabled", enabled)

def reset():
    serial_list = [control.device_serial_number()]
    choice_list = [0]
