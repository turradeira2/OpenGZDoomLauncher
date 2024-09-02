import tkinter as tk

# Função que será chamada quando o botão for clicado
def on_button_click():
     label1.config(text="Você clicou no botão!")

# Cria a janela principal
root = tk.Tk()
root.title("Janela com Containers Verticais")
root.geometry("400x300")

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
