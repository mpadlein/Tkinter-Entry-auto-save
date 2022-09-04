import tkinter as tk
from CustomWidget import EntryAutoSave

root = tk.Tk()

entry_1 = EntryAutoSave(
    name='entry_1',
    master=root
)
entry_2 = EntryAutoSave(
    name='entry_2',
    master=root
)
entry_3 = EntryAutoSave(
    name='entry_3',
    master=root
)

entry_1.pack()
entry_2.pack()
entry_3.pack()

root.mainloop()