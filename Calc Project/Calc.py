import tkinter as tk
reset_display=False  #Flag variable

#Function for click
def click(event):
    global reset_display
    current=entry.get()
    button_text=event.widget["text"]

    #logic for "C" button
    if button_text=='C':
        entry.delete(0,tk.END)
        entry.insert(tk.END,'0')
        reset_display=False

    elif button_text=='DEL':
        if current=='ERROR!':
            entry.delete(0,tk.END)
            entry.insert(tk.END,'0')
            reset_display=False
            return
        if len(current)<=1:
            entry.delete(0,tk.END)
            entry.insert(tk.END,'0')
            reset_display=False
            return
        current=current[:-1]
        entry.delete(0,tk.END)
        entry.insert(tk.END,current)
        reset_display=False


    elif button_text=='=':
        try:
            expression=current.replace('%','/100')
            result=eval(expression)
            entry.delete(0,tk.END)
            entry.insert(tk.END,result)
            reset_display=True
        except Exception:
            entry.delete(0,tk.END)
            entry.insert(tk.END,"ERROR!")
            reset_display=True

    else:
        if reset_display:
            entry.delete(0,tk.END)
            current=""
            reset_display=False
        if current=='0':
            current=''

        #avoid 2 consecutive operators
        operators="+-*/%"
        if current and current[-1] in operators and button_text in operators:
            current=current[:-1]

        if current=='' and button_text in "*/%":
            return
        
        entry.delete(0,tk.END)
        entry.insert(tk.END,current + button_text)


#Create a window and define its geometry
window=tk.Tk()
window.geometry("300x400")
window.resizable(width=False,height=False)
window.config(bg="#F0F0F0")

#Add title 
window.title("Simple Calculator")

#Entry Widget
entry=tk.Entry(window,bd=3,font=('Arial',20),justify='right',width=16,bg='#b6f2e9')
entry.pack(pady=10)
entry.insert(0,'0')

#Frame
frame=tk.Frame(window)
frame.pack()

#Define the buttons in a 2D array
buttons=[['C','DEL','/'],
         ['7','8','9','*'],
         ['4','5','3','-'],
         ['1','2','3','+'],
         ['.','0','%','=']]

#creating buttons for each character
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn=tk.Button(frame,text=buttons[i][j],bd=3,font=('Arial',16),width=3,height=1)
        btn.grid(row=i,column=j,padx=10,pady=10)
        btn.bind("<Button-1>",click)


window.mainloop()