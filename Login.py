import customtkinter as ctk
import FileManagerDelta as fileMan
import Analytics as analytics
import fileBroweser as browser
import complex64ReadWriter as complex
import time

currentuser = fileMan.user("Andrew", "Carvajal", "7641", ""," ")



class loginWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.focus()
        self.toplevel_window = None

        def button_click(args):
            if args == 1:
                print("login")

                self.destroy()
            if args == 2:
                print("login")
                fileMan.printUserArray()
                # if fileMan.log_in(self.log_firstname.get().strip(), self.log_phone.get().strip()):
                currentuser = None
                currentuser = fileMan.log_in(self.log_firstname.get().strip(), self.log_phone.get().strip())
                print("currentuser:", currentuser.fname)
                if currentuser != None:
                    self.open_fileBrowser(currentuser)

                    time.sleep(2.5)
                    self.destroy()
                else:
                    print("User ")
                    print(self.log_firstname.get())

        self.geometry("600x750")
        self.title("RF Scavenger Hunt Login")

        self.log_frame = ctk.CTkFrame(master=self)
        self.log_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.log_label = ctk.CTkLabel(self.log_frame, text="login ")
        self.log_label.pack(padx=20, pady=20)

        self.log_label_firstname = ctk.CTkLabel(self.log_frame, text="Enter you First Name")
        self.log_label_firstname.pack(padx=10, pady=10)

        self.log_firstname = ctk.CTkEntry(master=self.log_frame,
                                          placeholder_text="First Name")
        self.log_firstname.pack(pady=10, padx=10)

        self.log_label_lastname = ctk.CTkLabel(self.log_frame, text="Enter you Last Name")
        self.log_label_lastname.pack(padx=10, pady=10)

        self.log_lastname = ctk.CTkEntry(master=self.log_frame,
                                         placeholder_text="Last Name")
        self.log_lastname.pack(pady=10, padx=10)

        self.log_label_name = ctk.CTkLabel(self.log_frame,
                                           text="Enter Last 4 Digits of Phone Number")
        self.log_label_name.pack(padx=10, pady=10)

        self.log_phone = ctk.CTkEntry(master=self.log_frame,
                                      placeholder_text="last 4 digits Phone Number")
        self.log_phone.pack(pady=10, padx=10)

        self.log_label2 = ctk.CTkLabel(self.log_frame, text="Login")
        self.log_label2.pack(padx=20, pady=20)

        # self.login_button = customtkinter.CTkButton(self.log_frame,command=lambda: button_click(2) , text="Login")
        self.login_button = ctk.CTkButton(self.log_frame,
                                          command=lambda: button_click(2),
                                          text="Login")
        self.login_button.pack(pady=20)

        self.exit_button = ctk.CTkButton(self.log_frame,
                                         command=lambda: button_click(1),
                                         text="Exit")
        self.exit_button.pack(pady=20)

        self.toplevel_window = None

    def open_analytics(self):

        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = analytics.analytics()  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def open_fileBrowser(self, user):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = browser.Browser(user)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()  # if window exists focus it
