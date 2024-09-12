#Programa que imprime un texto simple con python.
#Autor: Dr. Aldo Gonzalez Vazquez
#Version: 1.0
#Fecha: 12/09/2024
import time

mensaje = "Feliz dia del programador ingenieros."

for i in range(len(mensaje)):
  print(mensaje[:i+1])
  time.sleep(0.2)
