import customtkinter as ctk
from tkinter import messagebox

def mostrar_sobre():
    """Exibe o alerta com as informações do criador."""
    messagebox.showinfo(
        title="Sobre o Aplicativo", 
        message="Desenvolvido por: FT Info\nVersão: 0.1\nTodos os direitos reservados © 2026"
    )