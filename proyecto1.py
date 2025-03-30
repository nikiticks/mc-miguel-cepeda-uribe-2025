#Gabriel Garcia Arias
#Juan Miguel Cepeda Uribe

import tkinter as tk
from tkinter import messagebox

def a_binario_entero(num):
    if num < 0:
        num = (1 << 32) + num
    return f'{num:032b}'

def a_binario_decimal(num):
    signo = '0' if num >= 0 else '1'
    num = abs(num)
    exponente = 127
    if num == 0:
        mantisa = '0' * 23
        exponente = '00000000'
    else:
        exponente_crudo = int(num).bit_length() - 1
        exponente = f'{exponente_crudo + 127:08b}'
        mantisa_cruda = num / (2 ** exponente_crudo) - 1
        mantisa = ''
        for _ in range(23):
            mantisa_cruda *= 2
            mantisa += str(int(mantisa_cruda))
            mantisa_cruda -= int(mantisa_cruda)
    return signo + exponente + mantisa

def calcular_resultado(operacion):
    try:
        resultado = eval(operacion)  
        if '.' in operacion:
            return resultado, a_binario_decimal(resultado)
        else:
            return resultado, a_binario_entero(int(resultado))
    except Exception as e:
        return f"Error: {e}", None

def ejecutar_calculo():
    operacion = entrada.get()
    resultado, binario = calcular_resultado(operacion)
    if binario:
        messagebox.showinfo("Resultado", f"Resultado: {resultado}\nBinario: {binario}")
    else:
        messagebox.showerror("Error", resultado)

ventana = tk.Tk()
ventana.title("Calculadora Binaria Simple")
ventana.geometry("300x150")

etiqueta = tk.Label(ventana, text="Escribe una operación:")
etiqueta.pack()

entrada = tk.Entry(ventana, width=30)
entrada.pack()

boton = tk.Button(ventana, text="Calcular", command=ejecutar_calculo)
boton.pack()

ventana.mainloop()
