import os
import tkinter as tk

ENTRIES_CACHE_FOLDER = os.path.join(os.getcwd(), 'entries-cache')

class EntryAutoSave(tk.Entry): 
    def __init__(self, name=None, *args, **kwargs) -> None:
        default_kwargs = {
            'relief': tk.SOLID,
            'justify': tk.CENTER,
            'font': ('', 12, '')
        }

        if name: 
            self.name = name
            self.path = os.path.join(ENTRIES_CACHE_FOLDER, self.name + '.txt')
            self.textvariable = tk.StringVar()
            default_kwargs['textvariable'] = self.textvariable

            self._load_entry()
            self.textvariable.trace_add('write', self._save_entry)

        default_kwargs.update(kwargs)  
        super().__init__(*args, **default_kwargs)


    def _save_entry(self, *args, **kwargs):
        try:
            if not self.name: return 
            file = open(self.path, mode='w', encoding='utf8')
            file.write(self.textvariable.get())
            file.close()
        except FileNotFoundError:
            if not os.path.isdir( ENTRIES_CACHE_FOLDER ):
                os.mkdir( ENTRIES_CACHE_FOLDER )


    def _load_entry(self):
            if not self.name: return
            if not os.path.isfile(self.path): return
            file = open(self.path, mode='r', encoding='utf8')
            content = file.read()
            file.close()
            self.textvariable.set(content)
        