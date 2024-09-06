import tkinter as tk
from tkinter import messagebox
import platform

os_name = platform.system()
print(os_name)

# Função que será chamada quando o botão for clicado
def on_button_click():
    label1.config(text="Você clicou no botão!")

def show_os():
    messagebox.showinfo("Curret OS",os_name)

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

# Configuração da janela principal
root = tk.Tk()
root.title("OpenGZDoomLauncher")
root.geometry("600x400")

#region menubar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Nova Janela", command=open_new_window)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit_app)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)
helpmenu.add_command(label="OS", command=show_os)
menubar.add_cascade(label="Ajuda", menu=helpmenu)

root.config(menu=menubar)
#endregion

# Criação e configuração dos containers (frames)
frame1 = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

frame2 = tk.Frame(root, bg="lightgreen", padx=10, pady=10)
frame2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

frame3 = tk.Frame(root, bg="lightcoral", padx=10, pady=10)
frame3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# Adiciona widgets aos containers
label1 = tk.Label(frame1, text="Container 1", bg="lightblue")
label1.grid(row=0, column=0, pady=10)

button1 = tk.Button(frame1, text="Botão 1", command=on_button_click)
button1.grid(row=1, column=0, pady=10)

label2 = tk.Label(frame2, text="Container 2", bg="lightgreen")
label2.grid(row=0, column=0, pady=10)

button2 = tk.Button(frame2, text="Botão 2", command=on_button_click)
button2.grid(row=1, column=0, pady=10)

label3 = tk.Label(frame3, text="Container 3", bg="lightcoral")
label3.grid(row=0, column=0, pady=10)

button3 = tk.Button(frame3, text="Botão 3", command=on_button_click)
button3.grid(row=1, column=0, pady=10)

# Configura a expansão das colunas para redimensionamento proporcional
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=1)

# Configura a expansão da linha para preencher a janela
root.grid_rowconfigure(0, weight=1)

# Inicia o loop principal do Tkinter
root.mainloop()
