import usb_hid
from adafruit_hid.mouse import Mouse
import time
import board
import digitalio
import rotaryio

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

mouse = Mouse(usb_hid.devices)


cc = ConsumerControl(usb_hid.devices)

keyboard = Keyboard(usb_hid.devices)

write_text = KeyboardLayoutUS(keyboard)



encoder = rotaryio.IncrementalEncoder(board.GP2, board.GP3)
last_position = 0


buttons = [board.GP12, board.GP19, board.GP28,
           board.GP13, board.GP18, board.GP22,
            board.GP14, board.GP17, board.GP21,
            board.GP15, board.GP16, board.GP20
           ]

key = [digitalio.DigitalInOut(pin_name) for pin_name in buttons]
for x in range(0,len(buttons)):
    key[x].switch_to_input(pull=digitalio.Pull.DOWN)


while True:

    if key[0].value:
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.LEFT_SHIFT,Keycode.B)
        time.sleep(0.3)
    elif key[1].value:
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.LEFT_SHIFT,Keycode.N)
        time.sleep(0.3)
    elif key[2].value:
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.LEFT_SHIFT,Keycode.M)
        time.sleep(0.3)
        
        
    elif key[3].value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Thonny\n')
        
    elif key[4].value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('VisualStudioCode\n')
        
    elif key[5].value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Spotify\n')
        
    elif key[6].value:
        print("pressed 4")
    elif key[7].value:
        print("pressed 5")
    elif key[8].value:
        print("pressed 6")
        
        
    elif key[9].value:
        print("pressed 7")
    elif key[10].value:
        print("pressed 8")
    elif key[11].value:
        print("pressed 9")

    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        print(current_position)
    elif position_change < 0:
        for _ in range(-position_change):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        print(current_position)
    last_position = current_position


