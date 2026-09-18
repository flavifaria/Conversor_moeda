import customtkinter as ctk

from pegar_moedas import nome_moedas
from pegar_moedas import conversoes_disponiveis
from pegar_conversoes import pegar_conversoes

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def centralizar_janela(janela, largura=600, altura=400):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")


janela = ctk.CTk()
centralizar_janela(janela, largura=500, altura=700)
janela.title("Conversor de Moeda")  # Define o título que aparece na janela



titulo = ctk.CTkLabel(janela, text="Conversor de Moeda", font=("Arial", 20))

texto_moeda_origem = ctk.CTkLabel(janela, text="Selecione a moeda de origem:")
campo_origem = ctk.CTkComboBox(janela, values=list(conversoes_disponiveis().keys()))

texto_moeda_destino = ctk.CTkLabel(janela, text="Selecione a moeda de destino:")
campo_destino = ctk.CTkComboBox(janela, values=list(conversoes_disponiveis().keys()))

texto_valor = ctk.CTkLabel(janela, text="Digite o valor:")
campo_valor = ctk.CTkEntry(janela, placeholder_text="Ex.: 100,00")

resultado = ctk.CTkLabel(janela, text="")

def converter_moeda():
    moeda_origem = campo_origem.get().strip().upper()
    moeda_destino = campo_destino.get().strip().upper()

    try:
        valor = float(campo_valor.get().replace(",", "."))
    except ValueError:
        resultado.configure(text="Digite um valor numérico válido.")
        return

    if not moeda_origem or not moeda_destino:
        resultado.configure(text="Selecione as moedas de origem e destino.")
        return

    taxas = pegar_conversoes(moeda_origem)
    taxa = taxas.get(moeda_destino) if taxas else None

    if taxa is None:
        resultado.configure(text="Não foi possível obter essa cotação.")
        return

    valor_convertido = valor * taxa
    resultado.configure(
        text=f"{valor:.2f} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}"
    )


botao_converter = ctk.CTkButton(janela, text="Converter", command=converter_moeda)


lista_moedas = ctk.CTkScrollableFrame(janela)

# Busca o dicionário com as moedas disponíveis
moedas_disponiveis = nome_moedas()

# Percorre todas as moedas e cria um texto para cada uma
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    label_moeda_disponivel = ctk.CTkLabel(
        lista_moedas,
        text=f"{codigo_moeda} - {nome_moeda}"
    )
    label_moeda_disponivel.pack()  # Coloca esse label dentro do frame


titulo.pack(pady=10, padx=10)
texto_moeda_origem.pack(pady=10, padx=3)
campo_origem.pack(pady=10)
texto_moeda_destino.pack(pady=10, padx=3)
campo_destino.pack(pady=10)
texto_valor.pack(pady=10, padx=3)
campo_valor.pack(pady=10)
botao_converter.pack(pady=10, padx=10)
resultado.pack(pady=10, padx=10)
lista_moedas.pack(pady=10, padx=10)

janela.mainloop()
