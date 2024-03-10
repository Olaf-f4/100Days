from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def typey():

    please = ('p', 'l', 'e', 'a', 's', 'e')
    for x in please:
        keyboard.press(f'{x}')
        keyboard.release(f'{x}')

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def printit():
    while True:
        time.sleep(5)
        typey()


printit()
