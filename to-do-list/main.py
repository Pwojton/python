import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title('To do list')


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title='Warning', message='You must enter the task!')


def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title='Warning', message='You must select a task you want to delete!')


def load_tasks():
    tasks = pickle.load(open("task.dat", "rb"))
    for task in tasks:
        listbox_task.insert(tkinter.END, task)


def save_tasks():
    tasks = listbox_task.get(0, listbox_task.size())
    pickle.dump(tasks, open("task.dat", "wb"))
    tkinter.messagebox.showinfo(title='Indo', message='Succesfuly saved')



# GUI creating
frame_task = tkinter.Frame(root)
frame_task.pack()

listbox_task = tkinter.Listbox(frame_task, height=30, width=70)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_task = tkinter.Entry(root, width=70)
entry_task.pack()

button_add_task = tkinter.Button(root, text='Add task', width=70, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text='Delete task', width=70, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text='Load task', width=70, command=load_tasks)
button_load_tasks.pack()

button_save_task = tkinter.Button(root, text='Save task', width=70, command=save_tasks)
button_save_task.pack()

root.mainloop()
