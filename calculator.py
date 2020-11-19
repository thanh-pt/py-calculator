import tkinter as tk

# command
def clickedEvent(e):
    print(e)

# GUI design
window = tk.Tk()
# Input
lbl_input = tk.Label(text="==CALCULATOR==",
                     bg='black',
                     fg='white',
                     font=('helvetica ', '24', 'bold'),
                     height=2)
lbl_input.pack(fill=tk.X)

# Key num
key_data = [
    ['AC','+/-','%','/'],
    ['7','8','9','x'],
    ['4','5','6','-'],
    ['1','2','3','+'],
    ['0',',','=']
]
frm_key_num = tk.Frame()
frm_key_num.pack()
for i in range(len(key_data)):
    for j in range(len(key_data[i])):
        frame = tk.Frame(
            master=frm_key_num,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        btn_num = tk.Button(master=frame,
                            width=10,
                            height=5,
                            text=key_data[i][j])
        btn_num.bind("<Button-1>", clickedEvent)
        btn_num.pack()

window.mainloop()
