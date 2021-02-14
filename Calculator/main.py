import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title('Calculator')

number_list = []
operators_list = []


def entry_number_1():
    calculator_entry.insert(tkinter.END, 1)
    number_list.append(1)


def entry_number_2():
    calculator_entry.insert(tkinter.END, 2)
    number_list.append(2)


def entry_number_3():
    calculator_entry.insert(tkinter.END, 3)
    number_list.append(3)


def entry_number_4():
    calculator_entry.insert(tkinter.END, 4)
    number_list.append(4)


def entry_number_5():
    calculator_entry.insert(tkinter.END, 5)
    number_list.append(5)


def entry_number_6():
    calculator_entry.insert(tkinter.END, 6)
    number_list.append(6)


def entry_number_7():
    calculator_entry.insert(tkinter.END, 7)
    number_list.append(7)


def entry_number_8():
    calculator_entry.insert(tkinter.END, 8)
    number_list.append(8)


def entry_number_9():
    calculator_entry.insert(tkinter.END, 9)
    number_list.append(9)


def entry_sum():
    calculator_entry.insert(tkinter.END, string='+')
    operators_list.append('+')


def equal():
    calculator_entry.delete(0, tkinter.END)
    for operator in operators_list:
        if operator == '+':
            sum_result = sum(number_list)
            calculator_entry.insert(tkinter.END, sum_result)
            del number_list[:]
            print(number_list)


# GUI
calculator_entry = tkinter.Entry(root, width=50)
calculator_entry.grid(row=0, columnspan=3)

button_sum = tkinter.Button(root, text=' +', width=10, command=entry_sum)
button_sum.grid(row=1, column=2, sticky='E')

button_1 = tkinter.Button(root, text='1', width=5, command=entry_number_1)
button_1.grid(row=1, column=0, sticky='W')

button_2 = tkinter.Button(root, text='2', width=5, command=entry_number_2)
button_2.grid(row=1, column=1, sticky='W')

button_3 = tkinter.Button(root, text='3', width=5, command=entry_number_3)
button_3.grid(row=1, column=2, sticky='W')

button_4 = tkinter.Button(root, text='4', width=5, command=entry_number_4)
button_4.grid(row=2, column=0, sticky='W')

button_5 = tkinter.Button(root, text='5', width=5, command=entry_number_5)
button_5.grid(row=2, column=1, sticky='W')

button_6 = tkinter.Button(root, text='6', width=5, command=entry_number_6)
button_6.grid(row=2, column=2, sticky='W')

button_7 = tkinter.Button(root, text='7', width=5, command=entry_number_7)
button_7.grid(row=3, column=0, sticky='W')

button_8 = tkinter.Button(root, text='8', width=5, command=entry_number_8)
button_8.grid(row=3, column=1, sticky='W')

button_9 = tkinter.Button(root, text='9', width=5, command=entry_number_9)
button_9.grid(row=3, column=2, sticky='W')

button_equal = tkinter.Button(root, text='=', width=10, command=equal)
button_equal.grid(row=2, column=2, sticky='E')

root.mainloop()
