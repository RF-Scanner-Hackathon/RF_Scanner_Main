import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plot
import CSVAlgoFoxtrot as goDelta
import complex64ReadWriter as complex
import Login as login


# csvpath = "test3.csv"


class analytics(ctk.CTkToplevel):
    def __init__(self, csvPath, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

        def button_click(args):
            # if args == 1:
            #    self.defaultTrace()
            if args == 3:
                print("exit button")
                self.destroy()

        # self.root = ctk.CTk()

        self.title("RF Analytics")
        self.geometry(f"{1500}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self,
                                          width=140,
                                          corner_radius=0)
        self.sidebar_frame.grid(row=0,
                                column=0,
                                rowspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.left_frame = ctk.CTkFrame(master=self,
                                       width=140,
                                       corner_radius=0)
        self.left_frame.grid(row=0,
                             column=4,
                             padx=100,
                             pady=100, sticky="nsew")

        self.mid_frame = ctk.CTkFrame(master=self,
                                      width=600,
                                      corner_radius=0)
        self.mid_frame.grid(row=0,
                            column=1,
                            padx=2,
                            pady=2,
                            rowspan=2,
                            columnspan=3, sticky="nsew")

        # self.right_frame = customtkinter.CTkFrame(self)
        # self.right_frame.grid(row=0, column=2, padx=(200, 200), pady=(20, 0), sticky="nsew")

        self.left_label = ctk.CTkLabel(master=self.left_frame,
                                       text="Zoom slider:",
                                       anchor="w")
        self.left_label.grid(row=2,
                             column=0,
                             padx=(20, 10),
                             pady=(10, 10),
                             sticky="nsew")

        #    self.right_label = customtkinter.CTkLabel(self.right_frame, text="right label:", anchor="w")
        #  self.right_label.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        self.slider = ctk.CTkSlider(master=self.left_frame,
                                    width=300,
                                    height=20,
                                    from_=1,
                                    to=1000,
                                    number_of_steps=999,
                                    command=self.update_surface)
        self.slider.grid(row=3,
                         column=0,
                         padx=(20, 10),
                         pady=(10, 10), sticky="nsew")
        goDelta.start(csvPath, 100, 50)

        self.left_label2 = ctk.CTkLabel(master=self.left_frame, text=("Max transmission:", goDelta.getMaxTranmission()))
        self.left_label2.grid(row=4,
                              column=0,
                              padx=(20, 10),
                              pady=(10, 10),
                              sticky="nsew")

        self.left_label3 = ctk.CTkLabel(master=self.left_frame, text=("Trace time:", goDelta.getTraceTime()))
        self.left_label3.grid(row=5,
                              column=0,
                              padx=(20, 10),
                              pady=(10, 10),
                              sticky="nsew")
        self.left_label4 = ctk.CTkLabel(master=self.left_frame, text=("noise floor", goDelta.getNoiseFloor()))
        self.left_label4.grid(row=6,
                              column=0,
                              padx=(20, 10),
                              pady=(10, 10),
                              sticky="nsew")
        self.left_label5 = ctk.CTkLabel(master=self.left_frame,
                                        text=("trans length average:", goDelta.getTranLengthAverage()))
        self.left_label5.grid(row=7,
                              column=0,
                              padx=(20, 10),
                              pady=(10, 10),
                              sticky="nsew")

        self.logo_label = ctk.CTkLabel(self.sidebar_frame,
                                       text="Analytics",
                                       font=ctk.CTkFont(size=20,
                                                        weight="bold"))
        # to change the apperance of the program
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame,
                                                  text="Appearance Mode:",
                                                  anchor="w")
        self.appearance_mode_label.grid(row=5,
                                        column=0,
                                        padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame,
                                                             values=["System", "Dark", "Light"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6,
                                              column=0,
                                              padx=20,
                                              pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        # this is the scalling of the program
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame,
                                                     values=["80%", "90%", "100%", "110%", "120%"],
                                                     command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8,
                                      column=0,
                                      padx=20, pady=(10, 20))
        # all the buttons in the right sidebar
        self.default_button = ctk.CTkButton(master=self.sidebar_frame,

                                            text="Default",

                                            command=lambda: self.defaultTrace(csvPath),
                                            text_color=("gray10", "#DCE4EE"))
        self.default_button.grid(row=0,
                                 column=0,
                                 padx=(5, 5),
                                 pady=(20, 20), sticky="nsew")

        self.edit_button = ctk.CTkButton(master=self.sidebar_frame,

                                         text="Edit",

                                         command=self.editTrace,
                                         text_color=("gray10", "#DCE4EE"))
        self.edit_button.grid(row=1,
                              column=0,
                              padx=(5, 5),
                              pady=(20, 20), sticky="nsew")
        self.save_button = ctk.CTkButton(master=self.sidebar_frame,
                                         text="Save",
                                         command=self.saveTrace,
                                         text_color=("gray10", "#DCE4EE"))
        self.save_button.grid(row=2,
                              column=0,
                              padx=(5, 5),
                              pady=(20, 20), sticky="nsew")

        self.load_button = ctk.CTkButton(master=self.sidebar_frame,
                                         text="Load",
                                         command=self.loadTrace,
                                         text_color=("gray10", "#DCE4EE"))
        self.load_button.grid(row=3,
                              column=0,
                              padx=(5, 5),
                              pady=(20, 20), sticky="nsew")
        # this is to exit the screen
        self.exit_button = ctk.CTkButton(master=self,
                                         text="Exit",
                                         command=lambda: button_click(3),
                                         text_color=("gray10", "#DCE4EE"))
        self.exit_button.grid(row=3,
                              column=4,
                              padx=(5, 5),
                              pady=(20, 20))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def defaultTrace(self, csvPath):
        print("default button")

        # spectrogram = complex.readArrayAsMatrix(csvPath)
        spectrogram = complex.genFromTextPassthrough(csvPath)

        print(spectrogram)

        plot.imshow(spectrogram, aspect='auto')
        plot.xlabel("Frequency [MHz]")
        plot.ylabel("Time [s]")
        plot.show()
        '''

        fileName = 'meetingCFILE.csv'
        spectrogram = np.loadtxt(open(fileName, "rb"), delimiter=",", skiprows=1)

        plot.imshow(spectrogram, aspect='auto')
        plot.xlabel("Frequency [MHz]")
        plot.ylabel("Time [s]")
        plot.show()'''
        # andrew.displayPSD(csvPath)
        '''
        fig, ax = plt.imshow()
        fig.set_size_inches(11, 5.3)
        global x, y, s, c
        x, y, s, c = np.random.rand(4, int(100))
        ax.scatter(x, y, s * self.slider.get(), c)
        ax.axis("off")
        fig.subplots_adjust(left=0,
                            right=1,
                            bottom=0,
                            top=1,
                            wspace=0,
                            hspace=0)
        canvas = FigureCanvasTkAgg(csv, master=self.mid_frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.33, rely=0.025)

        self.mid_frame.update()'''

    def update_surface(self, other):
        '''fig, ax = plt.subplots()
        fig.set_size_inches(11, 5.3)
        ax.scatter(x, y, s * self.slider.get(), c)
        ax.axis("off")
        fig.subplots_adjust(left=0,
                            right=1,
                            bottom=0,
                            top=1,
                            wspace=0,
                            hspace=0)
        canvas = FigureCanvasTkAgg(csv, master=self.mid_frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.33, rely=0.025)
        self.mid_frame.update()'''

    def editTrace(self):
        print("edit button")

    def saveTrace(self):
        print("save button")

    def loadTrace(self):
        print("load button")
