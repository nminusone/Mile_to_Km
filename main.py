from tkinter import *


def calc_km():
    miles = mile_input.get()
    conversion = int(miles) * 1.609
    conversion_label.config(text=conversion)
    print(conversion)


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=200)
window.config(padx=100, pady=20)

mile_input = Entry(width=5)
mile_input.grid(row=0, column=1)
# content = StringVar()
# content.set('')
mile_input.get()

mile_label = Label(text='Miles')
mile_label.grid(row=0, column=2)
mile_label.config(pady=20)

equal_label = Label(text='is equal to')
equal_label.grid(row=1, column=0)

conversion_label = Label(text='0')
conversion_label.grid(row=1, column=1)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

calc_button = Button(text='Calculate', command=calc_km)
calc_button.grid(row=2, column=1)

window.mainloop()
