# import filedialog module
import os
from tkinter import filedialog
import customtkinter as ctk
import Analytics as analytics
import FileManagerDelta as fileMan
import complex64ReadWriter as complex
import time
CSVAlgoCopyPath = os.path.abspath('CSVAlgoDelta.py')

###Mostly Copied over from file browser.py
class loadNewAnalytics(ctk.CTkToplevel):
    returnFile = None

    def __init__(self, analyticsWindow, algoPath,csvPath, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.toplevel_window = None

        def button_click(args): #Submit Button
            if args == 1:
                print("Ok")
                if(algoPath == CSVAlgoCopyPath):
                    self.open_analytics(csvPath,'d')
                else:
                    self.open_analytics(csvPath, 'y')
                analyticsWindow.destroy()
                self.destroy()

        self.geometry("700x400")
        self.title("Confirm Load")

        # Function for opening the
        # file explorer window
        def noOption():
            self.destroy()

        self.file = ctk.CTkFrame(master=self)
        self.file.pack(pady=20, padx=100, fill="both", expand=True)

        # Create a File Explorer label
        self.label_file_explorer = ctk.CTkLabel(self.file,
                                                text="Confirm Load of " + os.path.basename(algoPath),
                                                width=100, height=4)
        self.label_file_explorer.pack(padx=20, pady=20)

        self.button_explore = ctk.CTkButton(self.file,
                                            text="No",
                                            command=noOption)
        self.button_explore.pack(padx=20, pady=20)

        self.button_exit = ctk.CTkButton(self.file,
                                         text="Ok",
                                         command=lambda: button_click(1))
        self.button_exit.pack(padx=20, pady=20)

    # Let the window wait for any events

    def open_analytics(self, csvPath, DefaultBool):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = analytics.analytics(csvPath,DefaultBool)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


    def get_fileName(self):
        if (self.returnFile == None):
            return None
        else:
            return self.returnFile


'''
        self.label_file_explorer.grid(column=2, row=1, padx=(5, 5),
                                      pady=(20, 20))

        self.button_explore.grid(column=2, row=2, padx=(5, 5),
                                 pady=(20, 20))

        self.button_exit.grid(column=2, row=3, padx=(5, 5),
                              pady=(20, 20))
'''
'''
if __name__ == "__main__":
    app = Browser()
    app.mainloop()
'''
