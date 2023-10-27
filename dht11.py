import Adafruit_DHT
import tkinter as tk

# Función para actualizar la temperatura
def actualizar_temperatura():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        temperatura_label.config(text=f'Temperatura: {temperature:.1f}°C\nHumedad: {humidity:.1f}%')
    else:
        temperatura_label.config(text='Error al leer el sensor. Intenta nuevamente.')

    # Programar la actualización periódica
    ventana.after(10, actualizar_temperatura)  # Actualiza cada 5 segundos (5000 ms)

# Configurar la ventana
ventana = tk.Tk()
ventana.title("Temperatura y Humedad")

# Define el pin al que está conectado el sensor (ejemplo: GPIO17)
pin = 2

# El sensor es DHT11, pero puedes cambiarlo a DHT22 si estás utilizando ese sensor
sensor = Adafruit_DHT.DHT11

# Crear una etiqueta para mostrar la temperatura
temperatura_label = tk.Label(ventana, font=("Arial", 24))
temperatura_label.pack(padx=20, pady=20)

# Iniciar la actualización de la temperatura
actualizar_temperatura()

ventana.mainloop()