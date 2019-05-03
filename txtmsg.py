#!/usr/bin/env python3

"""
APOGEE Tkinter Textarea & Messagebox

In this script, we create a simple tkinter 
textarea and put the text on messagebox

Author: M. Fauzilkamil Zainuddin
Last modified: May 2019
Website: http://coderstalk.blogspot.com
"""

import tkinter as tk
from tkinter import messagebox as msg

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_master()

        self.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def init_master(self):
        self.master.geometry("500x300+300+300") # window size
        self.master.title("Sistem APOGEEK") # the dialog title

    def create_widgets(self):
        # this is the UI creation
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        self.label = tk.Label(self, text="Sila masukkan komen:")
        self.label.grid(sticky=tk.W, pady=4, padx=5)

        self.txtarea = tk.Text(self, bg="#eeeeee")
        self.txtarea.grid(row=1, column=0, columnspan=2, rowspan=4,
            padx=5, sticky=tk.E+tk.W+tk.S+tk.N)

        self.simpanbtn = tk.Button(self, text="Simpan", command=self.baca_komen)
        self.simpanbtn.grid(row=1, column=3)

        self.tutupbtn = tk.Button(self, text="Tutup", command=self.master.destroy)
        self.tutupbtn.grid(row=2, column=3, pady=4)

        self.okbtn = tk.Button(self, text="OK", command=self.master.destroy)
        self.okbtn.grid(row=5, column=3)

    def baca_komen(self):
        # read the comment
        self.komen = self.txtarea.get('1.0','end-1c')

        if not self.komen:
            self.komen = 'Sila taip di ruang komen'

        msg.showinfo("Komen", self.komen, icon="warning")

    def buat_taktau(self):
        msg.showinfo("Tak Tahu", "Takde fungsi lagi, buat tak tau je lah")

apogeek = tk.Tk()

app = Application(master=apogeek)
app.mainloop()
