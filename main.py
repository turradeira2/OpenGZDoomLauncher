#region imports
import tkinter as tk
from tkinter import messagebox
#endregion

#region vars
#endregion

# Função que será chamada quando o botão for clicado
def on_button_click():
    label1.config(text="Você clicou no botão!")

# Função para exibir a mensagem "Sobre"
def show_about():
    messagebox.showinfo("Sobre", "Este é um exemplo de aplicação Tkinter com menubar.")

# Função para abrir uma nova janela
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Nova Janela")
    new_window.geometry("200x150")
    tk.Label(new_window, text="Esta é uma nova janela.").pack(pady=20)

# Função para sair da aplicação
def quit_app():
    root.quit()

# Cria a janela principal
root = tk.Tk()
root.title("Janela com Containers Verticais")
root.geometry("400x300")

#region menubar
menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Nova Janela", command=open_new_window)  # Corrigido para "label"
filemenu.add_separator()
filemenu.add_command(label="Sair", command=quit_app)  # Corrigido para "label"
menubar.add_cascade(label="Arquivo", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Sobre", command=show_about)  # Corrigido para "label"
menubar.add_cascade(label="Ajuda", menu=helpmenu)

root.config(menu=menubar)
#endregion

# Cria o primeiro container vertical
frame1 = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame1.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

# Adiciona widgets ao primeiro container
label1 = tk.Label(frame1, text="Container 1", bg="lightblue")
label1.pack(pady=10)

button1 = tk.Button(frame1, text="Botão 1", command=on_button_click)
button1.pack(pady=10)

# Cria o segundo container vertical
frame2 = tk.Frame(root, bg="lightgreen", padx=10, pady=10)
frame2.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

# Adiciona widgets ao segundo container
label2 = tk.Label(frame2, text="Container 2", bg="lightgreen")
label2.pack(pady=10)

button2 = tk.Button(frame2, text="Botão 2", command=on_button_click)
button2.pack(pady=10)

# Cria o terceiro container vertical
frame3 = tk.Frame(root, bg="lightcoral", padx=10, pady=10)
frame3.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

# Adiciona widgets ao terceiro container
label3 = tk.Label(frame3, text="Container 3", bg="lightcoral")
label3.pack(pady=10)

button3 = tk.Button(frame3, text="Botão 3", command=on_button_click)
button3.pack(pady=10)

# Inicia o loop principal do Tkinter
root.mainloop()