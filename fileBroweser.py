# import filedialog module
from tkinter import filedialog
import customtkinter as ctk
import Analytics as analytics
import FileManagerDelta as fileMan
import complex64ReadWriter as complex
import time


class Browser(ctk.CTkToplevel):
    returnFile = None

    def __init__(self, currentuser, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.toplevel_window = None

        def button_click(args):
            if args == 1:
                print("Submit")

                # self.open_analytics()
                # time.sleep(2.5)

                sam = fileMan.save_file(currentuser, self.filename)
                print("sams fileMan: ", sam)
                self.absolutePath = complex.iqToCSV(sam)
                self.open_analytics(self.absolutePath)
                #self.open_analytics(self.filename)
                self.destroy()

        self.geometry("700x400")
        self.title("File Explorer")

        # Function for opening the
        # file explorer window
        def browseFiles():
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.filename = filedialog.askopenfilename(initialdir=currentuser.getPath(),
                                                           title="Select a CSV File",
                                                           filetypes=(("all files",
                                                                       "*.*"),
                                                                      ("iq files",
                                                                       "*.iq*"),
                                                                      ("CSV files",
                                                                       "*.csv*")))

                self.label_file_explorer.configure(text="File Opened: " + self.filename)
                # time.sleep(2.5)
                # self.destroy()
            else:
                self.toplevel_window.focus()  # if window exists focus it

            return self.filename

        self.file = ctk.CTkFrame(master=self)
        self.file.pack(pady=20, padx=100, fill="both", expand=True)

        # Create a File Explorer label
        self.label_file_explorer = ctk.CTkLabel(self.file,
                                                text="File Explorer",
                                                width=100, height=4)
        self.label_file_explorer.pack(padx=20, pady=20)

        self.button_explore = ctk.CTkButton(self.file,
                                            text="Browse Files",
                                            command=browseFiles())
        self.button_explore.pack(padx=20, pady=20)

        self.button_exit = ctk.CTkButton(self.file,
                                         text="Submit",
                                         command=lambda: button_click(1))
        self.button_exit.pack(padx=20, pady=20)

    # Let the window wait for any events

    def open_analytics(self, csvPath):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = analytics.analytics(csvPath)  # create window if its None or destroyed
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
