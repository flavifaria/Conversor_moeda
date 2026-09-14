#Janela 500x500
#Titulo: Conversor de Moeda
#Campos de selecionar moedas ->origem
#botão de converter
#Mostrar o resultado da conversão

#importar a biblioteca tkinter
import customtkinter as ctk
from pegar_moedas import nome_moedas
from pegar_moedas import conversoes_disponiveis

ctk.set_appearance_mode("dark")
caset = ctk.set_default_color_theme("green")


#criar a nossa janela e configurar
janela = ctk.CTk()
janela.geometry("500x500")
janela.title("Conversor de Moeda")

#criar os botões,textos e elementos
titulo = ctk.CTkLabel(janela, text="Conversor de Moeda", font=("Arial", 20))

texto_moeda_origem = ctk.CTkLabel(janela, text="Selecione a moeda de origem:")
campo_origem = ctk.CTkComboBox(janela, values=list(conversoes_disponiveis().keys()))

texto_moeda_destino = ctk.CTkLabel(janela, text="Selecione a moeda de destino:")
campo_destino = ctk.CTkComboBox(janela, values=list(conversoes_disponiveis().keys()))

#função para converter a moeda
def converter_moeda():
    print("Converter moeda...")

botao_converter = ctk.CTkButton(janela, text="Converter" ,command=converter_moeda)

lista_moedas = ctk.CTkScrollableFrame(janela)

moedas_disponiveis = nome_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    label_moeda_disponivel = ctk.CTkLabel(lista_moedas, text=f"{codigo_moeda} - {nome_moeda}" )
    label_moeda_disponivel.pack()


#colocar os elementos na janela
titulo.pack(pady=10,padx=10)
texto_moeda_origem.pack(pady=10,padx=3)
campo_origem.pack(pady=10)
texto_moeda_destino.pack(pady=10,padx=3)
campo_destino.pack(pady=10)
botao_converter.pack(pady=10,padx=10)
lista_moedas.pack(pady=10,padx=10)


#rodar a janela
janela.mainloop()
