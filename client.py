radio.set_group(69)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)

input.on_button_pressed(Button.A, ChangeVote)
input.on_button_pressed(Button.B, SendVote)

vote = -1
enabled = 0

def ChangeVote():
    global vote
    vote = (vote + 1) % 4
    basic.show_string(String.from_char_code(vote+65), 0)

def SendVote():
    if enabled == 1:
        radio.send_value("vote", vote+1)

def on_received_value(name, value):
    global enabled
    if name == "enabled":
        if value == 1: enabled = 1
        if value == 0: enabled = 0
radio.on_received_value(on_received_value)
