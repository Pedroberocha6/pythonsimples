import tkinter as tk

window = tk.Tk()
window.geometry("300x150")
window.title("Gerencia frase")

# Adicionar um Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="x", expand = True)

# Adicionar o Label  
label = tk.Label(frame, text = "ola mundo")
label.pack(fill= 'x', expand =True)

# adicionar o input text 
frase = tk.Label(frame, text ="Frase")
frase.pack(fill = 'x', expand=True)

fraseInp = tk.Entry(frame)
fraseInp.pack(fill="x", expand = True)

# Alterar label
def click():
    label.config(text=fraseInp.get())

# Adicionar botao
button = tk.Button(frame, text = "Enviar", command= click)
button.pack()


    

window.mainloop()