import tkinter as gui

def truncar(x):
    somatoria = int(x * 100) / 100
    return somatoria

def calculadora_imc():
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())

    soma = peso / (altura * altura)

    resultado_imc = truncar(soma)
    result = 0
    resultado_label.config(text=f'{resultado_imc}')

janela = gui.Tk()
janela.title('Calculadora de IMC')
janela.geometry('290x130')

entrada_peso = gui.Label(janela, text='PESO:')
entrada_peso.grid(row=0, column=0)

entrada_peso = gui.Entry(janela, width=30)
entrada_peso.grid(row=0, column=1)

entrada_altura = gui.Label(janela, text='ALTURA:')
entrada_altura.grid(row=1, column=0)

entrada_altura = gui.Entry(janela, width=30)
entrada_altura.grid(row=1, column=1, sticky='w')

resultado_button = gui.Button(janela, text='CALCULAR', command=calculadora_imc)
resultado_button.grid(row=2, column=0, padx=5, pady=20, rowspan=2)

resultado_label = gui.Label(janela, text='')
resultado_label.grid(row=2, column=1, padx=5, pady=20, rowspan=2)

janela.mainloop()