import keyboard

async def hotkey_listener():
    while True:
        if keyboard.is_pressed('ctrl+win+z'):
            print('You Pressed ctrl+win+z')
            break