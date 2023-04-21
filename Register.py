import customtkinter as ctk
import FileManagerDelta as fileMan
import time


class registerWindow(ctk.CTkToplevel):
    def __init__(self, lastname=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("500x650")
        self.title("RF Scavenger Hunt Register")

        def button_click(args):
            if args == 2:
                print("submit")
                fileMan.create_folder(self.firstNameEntry.get(), self.lastName.get(), self.phone.get())
                fileMan.loadUserArray()

                time.sleep(2.5)
                self.destroy()

            if args == 3:
                print("exit button")
                self.destroy()

        self.reg_frame = ctk.CTkFrame(master=self)
        self.reg_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.reg_label = ctk.CTkLabel(self.reg_frame, text="Register")
        self.reg_label.pack(padx=20, pady=20)

        self.reg_label_name = ctk.CTkLabel(self.reg_frame,
                                           text="Enter First Name")
        self.reg_label_name.pack(padx=10, pady=10)

        self.firstNameEntry = ctk.CTkEntry(master=self.reg_frame,
                                           placeholder_text="First Name")
        self.firstNameEntry.pack(pady=10, padx=10)

        self.reg_label_lastname = ctk.CTkLabel(self.reg_frame,
                                               text="Enter Last Name")
        self.reg_label_lastname.pack(padx=10, pady=10)

        self.lastName = ctk.CTkEntry(master=self.reg_frame,
                                     placeholder_text="Last Name")
        self.lastName.pack(pady=10, padx=10)

        self.reg_label_name = ctk.CTkLabel(self.reg_frame,
                                           text="Enter Last 4 Digits of Phone Number")
        self.reg_label_name.pack(padx=10, pady=10)

        self.phone = ctk.CTkEntry(master=self.reg_frame,
                                  placeholder_text="Last 4 Digits of Phone Number")
        self.phone.pack(pady=10, padx=10)

        self.submit_button = ctk.CTkButton(self.reg_frame,
                                           command=lambda: button_click(2),
                                           text="Submit")
        self.submit_button.pack(pady=20)

        self.exit_button = ctk.CTkButton(self.reg_frame,
                                         command=lambda: button_click(3),
                                         text="Exit")
        self.exit_button.pack(pady=20)

        # fileMan.create_folder(fileMan.participant_info(str(self.firstName), str(self.lastName), str(self.phone)))
