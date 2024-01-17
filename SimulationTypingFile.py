# python .\SimulationTypingFile.py

from pynput.keyboard import Controller
import time

# Crea un objeto Controller para simular el teclado
keyboard = Controller()

# Espera un tiempo antes de comenzar a escribir
time.sleep(10)  # Espera 10 segundos

# Abre el archivo y simula la escritura
file_path = r"D:\osvaldohm\Desktop\info to pass.txt"
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()  # Elimina saltos de línea
        keyboard.type(line)
        keyboard.press('\n')  # Simula la tecla Enter
        keyboard.release('\n')
        time.sleep(0.2)  # Espera 0.2 segundos entre líneas

print("Proceso completado.")
