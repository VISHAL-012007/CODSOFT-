import tkinter as tk 
from tkinter import messagebox
import json
import os

data="tasks.json"
edit_index=None
#function for loading tasks
def load_tasks():
    if os.path.exists(data):
        with open(data, 'r') as f:
            try:
                tasks=json.load(f)
                for task in tasks:
                    listbox.insert(tk.END,task)
            except json.JSONDecodeError:
                pass



#function for saving tasks
def save_tasks():
    tasks=listbox.get(0,tk.END)
    with open(data, 'w') as f:
        json.dump(tasks,f,indent=4)

#function for adding task
def add_task(event=None):
    global edit_index
    task=entry.get().strip()
    existing_tasks=listbox.get(0,tk.END)
    if task=="":
        messagebox.showerror("Error","Enter a valid task")
        return
    if edit_index is None:
        if task in existing_tasks:
            messagebox.showerror("Error","Task already exists!")
            return
        listbox.insert(tk.END,task)
    else:
        listbox.delete(edit_index)
        listbox.insert(edit_index,task)
        edit_index=None
    entry.delete(0,tk.END)
    save_tasks()

#function for deleting a task
def delete_task():
    selected_task=listbox.curselection()
    if not selected_task:
        messagebox.showerror("Error","Select atleast one task")
    confirm=messagebox.askyesno("Confirm delete","Are you sure want to delete the task")
    if confirm:
        for index in reversed(selected_task):
            listbox.delete(index)
        save_tasks()
    
#Function for editing a task
def edit_tasks():
    global edit_index
    selected_task=listbox.curselection()
    if not selected_task:
        messagebox.showerror("Error","Select atleast one task")
        return
    edit_index=selected_task[0]
    task_text=listbox.get(edit_index)
    entry.delete(0,tk.END)
    entry.insert(0,task_text)
    entry.focus()

#Function for task completed
def mark_done():
    selected_task=listbox.curselection()
    if not selected_task:
        messagebox.showerror("Error","Select atleast one task")
        return
    for index in selected_task:
        task=listbox.get(index)
        if task.startswith("✔"):
            new_task=task[2:]
        else:
            new_task="✔ "+task
        listbox.delete(index)
        listbox.insert(index,new_task)
    save_tasks()
    


window=tk.Tk()

#Define the geometry for the window
window.geometry("420x420")
window.resizable(width=False,height=False)
window.config(bg="#f2f2f2")

#Add the title
window.title("To Do List")

#Add icon for title
window.iconbitmap(r"C:\Users\divya\Documents\Desktop files\VS CODE\to-do-list.ico")

#Entry Box
entry=tk.Entry(window,width=30,relief="groove")
entry.bind("<Return>",add_task)
entry.pack(padx=10,pady=20)

#Button Styling
button_style={"bg": "#e0e0e0","fg": "black","activebackground": "#d5d5d5","bd": 0,"width": 15}

#Add Button
add_button=tk.Button(window,text="Add Task",command=add_task,**button_style)
add_button.pack()

#Delete Button
delete_button=tk.Button(window,text="Delete Task",command=delete_task,**button_style)
delete_button.pack(pady=20)

#Edit Button
edit_button=tk.Button(window,text="Edit Task",command=edit_tasks,**button_style)
edit_button.pack()

#Mark Done Button
done_button=tk.Button(window,text="Mark Done",command=mark_done,**button_style)
done_button.pack(pady=20)

#Listbox
listbox=tk.Listbox(window,width=50,height=15,bg="white",selectbackground="#000000",activestyle="dotbox",bd=0,selectmode=tk.MULTIPLE)
listbox.bind("<Double-Button-1>",lambda event:delete_task())
listbox.pack(pady=15)

load_tasks()
window.mainloop()