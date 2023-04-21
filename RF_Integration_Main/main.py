import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Register as registerWindow
import Login as loginWindow
import FileManagerDelta as fileMan


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fileMan.__init__(self)
        print(fileMan.loadUserArray())
        self.geometry("800x600")
        self.title("RF Scavenger Hunt")

        self.frame_1 = ctk.CTkFrame(master=self)
        self.frame_1.pack(pady=20,
                          padx=60,
                          fill="both",
                          expand=True)

        self.label_1 = ctk.CTkLabel(master=self.frame_1,
                                    justify=ctk.LEFT,
                                    text="Welcome to the RF Scavenger Hunt ")
        self.label_1.pack(pady=10, padx=10)
        # asks new users to register
        self.label_2 = ctk.CTkLabel(master=self.frame_1,
                                    justify=ctk.LEFT,
                                    text="If you are new please register!")
        self.label_2.pack(pady=10, padx=10)

        self.button_1 = ctk.CTkButton(master=self.frame_1,
                                      text="Register",
                                      command=self.open_register)
        self.button_1.pack(side="top",
                           padx=20,
                           pady=20)

        self.label_3 = ctk.CTkLabel(master=self.frame_1,
                                    justify=ctk.LEFT,
                                    text="Returning user please login!")
        self.label_3.pack(pady=10, padx=10)

        self.button_2 = ctk.CTkButton(master=self.frame_1,
                                      text="login",
                                      command=self.open_login)
        self.button_2.pack(side="top",
                           padx=20,
                           pady=20)

        self.label_4 = ctk.CTkLabel(master=self.frame_1,
                                    justify=ctk.LEFT,
                                    text="Appearance Mode:")
        self.label_4.pack(pady=5, padx=5)

        self.scaling_optionemenu = ctk.CTkOptionMenu(self.frame_1,
                                                     values=["80%", "90%", "100%", "110%", "120%"],
                                                     command=self.change_scaling_event)
        self.scaling_optionemenu.pack(side="top",
                                      padx=5,
                                      pady=5)

        self.label_5 = ctk.CTkLabel(master=self.frame_1,
                                    justify=ctk.LEFT,
                                    text="UI Scaling:")
        self.label_5.pack(pady=5, padx=5)

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.frame_1,
                                                             values=["System", "Dark", "Light"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.pack(side="top",
                                              padx=5,
                                              pady=5)

        self.toplevel_window = None

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def open_register(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = registerWindow.registerWindow()  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def open_login(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = loginWindow.loginWindow()  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


if __name__ == "__main__":
    app = App()
    app.mainloop()
