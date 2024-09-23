#region imports
import tkinter as tk
from tkinter import messagebox
import platform
#endregion

#region vars
wad_location= "test"
os_name = platform.system()
print(os_name)
#endregion


#region window functions
def on_button_click():
    label1.config(text="Você clicou no botão!")

def show_os():
    messagebox.showinfo("Curret OS",os_name)

#region About box
def show_about():
    messagebox.showinfo("About", "This is the About Message Box!")
#endregion

#region wad folder menu
def wad_location_select():
    messagebox.showinfo("WAD LOCATION",wad_location)
    print(wad_location)
#endregion

# Função para abrir uma nova janela
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Nova Janela")
    new_window.geometry("200x150")
    tk.Label(new_window, text="Esta é uma nova janela.").pack(pady=20)

# Função para sair da aplicação
def quit_app():
    root.quit()
#endregion

#region root window
root = tk.Tk()
root.title("OpenGZDoomLauncher")
root.geometry("600x400")
#endregion

#region menubar
menubar = tk.Menu(root)

#region file menu
filemenu = tk.Menu(menubar, tearoff=0)

filemenu.add_command(label="WADs Location", command=wad_location_select)
filemenu.add_separator()

filemenu.add_command(label="Nova Janela", command=open_new_window)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=quit_app)
menubar.add_cascade(label="File", menu=filemenu)
#endregion

#region help menu
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)
helpmenu.add_command(label="OS", command=show_os)
menubar.add_cascade(label="Ajuda", menu=helpmenu)
#endregion

root.config(menu=menubar)
#endregion

#region frames
wadframe = tk.Frame(root, bg="lightblue", padx=10, pady=10)
wadframe.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

frame2 = tk.Frame(root, bg="lightgreen", padx=10, pady=10)
frame2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

frame3 = tk.Frame(root, bg="lightcoral", padx=10, pady=10)
frame3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
#endregion

#region WAD frame
testvar = ('doom','doom 2','sigil','sigil 2')
wadvar = tk.Variable(value=testvar) 

wadlist = tk.Listbox(wadframe,listvariable=wadvar,height=4,selectmode=tk.EXTENDED )
wadlist.grid(row=0, column=0,pady=10)
#endregion

#region widgets
label1 = tk.Label(wadframe, text="Container 1", bg="lightblue")
label1.grid(row=2, column=0, pady=10)

button1 = tk.Button(wadframe, text="Botão 1", command=on_button_click)
button1.grid(row=1, column=0, pady=10)

label2 = tk.Label(frame2, text="Container 2", bg="lightgreen")
label2.grid(row=0, column=0, pady=10)

button2 = tk.Button(frame2, text="Botão 2", command=on_button_click)
button2.grid(row=1, column=0, pady=10)

label3 = tk.Label(frame3, text="Container 3", bg="lightcoral")
label3.grid(row=0, column=0, pady=10)

button3 = tk.Button(frame3, text="Botão 3", command=on_button_click)
button3.grid(row=1, column=0, pady=10)
#endregion

#region grid config
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=1)

root.grid_rowconfigure(0, weight=1)
#endregion

root.mainloop()