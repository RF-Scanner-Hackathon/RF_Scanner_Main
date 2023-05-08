import importlib.util
import os

import customtkinter as ctk
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import complex64ReadWriter as complex
import Login as login
import loadNewAnalytics
import os
import importlib.util

# csvpath = "test3.csv"
CSVAlgoCopyPath = os.path.abspath('CSVAlgoDelta.py')
CSVAlgoDefaultName = "CSVAlgoDelta"

#csvPathTest = "test3.csv"
canvas = FigureCanvasTkAgg
userDirectory = " "
userAlgoPath = " "
sliderLastNumber = 0


class ScrollingFrameSean(ctk.CTkScrollableFrame):
    listSize = 0

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...

    def addText(self, text):
        self.label = ctk.CTkLabel(master=self, text=(text))
        self.label.grid(row=self.listSize, column=0, padx=20)
        self.listSize = self.listSize + 1

    def addTextArray(self, array):
        for index in array:
            self.addText(index)
        self.addText(" ")
        self.addText(" ")


def algoImport(algoPath):
    importName = os.path.basename(algoPath)
    # specImport = importlib.util.sp
    try:
        # fp,path,desc = imp.find_module(importName,algoPath)
        specImport = importlib.util.spec_from_file_location(importName, algoPath)
        print("Loaded Algorithm " + algoPath)
        return specImport.loader.load_module()
    except:
        print("Module not found: " + algoPath + " " + importName)
        # fp, path, desc = imp.find_module(CSVAlgoDefaultName)
        # return imp.load_module(CSVAlgoDefaultName,fp,path,desc)
        specImport = importlib.util.spec_from_file_location(CSVAlgoDefaultName, CSVAlgoCopyPath)
        print(CSVAlgoCopyPath)
        return specImport.loader.load_module()
    return none
    # return imp.load_module(importName,fp,path,desc)


class analytics(ctk.CTkToplevel):
    def __init__(self, csvPath, algoBoolean, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__.update(kwargs)
        self.toplevel_window = None
        global csvPathTest
        csvPathTest = csvPath
        # algoPath = pathlib.Path(csvPath).parent.resolve().__str__()
        algoPath = os.path.dirname(csvPath)
        global userDirectory
        userDirectory = algoPath
        importName = os.path.basename(algoPath)
        algoPath += "/"
        algoPath += importName
        algoPath += "Algo.py"
        global userAlgoPath
        userAlgoPath = algoPath
        if (algoBoolean == "y"):

            # print(algoPath)
            goDelta = algoImport(algoPath)
        else:
            goDelta = algoImport(CSVAlgoCopyPath)

        global csvPathTest
        csvPathTest = csvPath
        # algoPath = pathlib.Path(csvPath).parent.resolve().__str__()
        algoPath = os.path.dirname(csvPath)
        global userDirectory
        userDirectory = algoPath
        importName = os.path.basename(algoPath)
        algoPath += "/"
        algoPath += importName
        algoPath += "Algo.py"
        global userAlgoPath
        userAlgoPath = algoPath
        if (algoBoolean == "y"):

            # print(algoPath)
            goDelta = algoImport(algoPath)
        else:
            goDelta = algoImport(CSVAlgoCopyPath)

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
                             pady=0, sticky="nsew")

        self.mid_frame = ctk.CTkFrame(master=self,
                                      width=600,
                                      corner_radius=0)
        self.mid_frame.grid(row=0,
                            column=1,
                            padx=2,
                            pady=2,
                            rowspan=3,
                            columnspan=3, sticky="nsew")

        

        self.left_label = ctk.CTkLabel(master=self.left_frame,
                                       text="Zoom slider:",
                                       anchor="w")
        self.left_label.grid(row=2,
                             column=0,
                             padx=(20, 10),
                             pady=(5, 2),
                             sticky="nsew")

        #    self.right_label = customtkinter.CTkLabel(self.right_frame, text="right label:", anchor="w")
        #  self.right_label.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        self.slider = ctk.CTkSlider(master=self.left_frame,
                                    width=300,
                                    height=20,
                                    from_=0,
                                    to=4,
                                    number_of_steps=4,
                                    command=self.update_surface)
        self.slider.grid(row=3,
                         column=0,
                         padx=(20, 10),
                         pady=(10, 5), sticky="nsew")
        goDelta.start(csvPath, 100, 50)

        self.left_label2 = ctk.CTkLabel(master=self.left_frame, text=("Max transmission:", goDelta.getMaxTranmission()))
        self.left_label2.grid(row=4,
                              column=0,
                              padx=(20, 10),
                              pady=(5, 5),
                              sticky="nsew")

        self.left_label3 = ctk.CTkLabel(master=self.left_frame, text=("Trace time:", goDelta.getTraceTime()))
        self.left_label3.grid(row=5,
                              column=0,
                              padx=(20, 10),
                              pady=(5, 5),
                              sticky="nsew")
        self.left_label4 = ctk.CTkLabel(master=self.left_frame, text=("noise floor", goDelta.getNoiseFloor()))
        self.left_label4.grid(row=6,
                              column=0,
                              padx=(20, 10),
                              pady=(5, 5),
                              sticky="nsew")
        self.left_label5 = ctk.CTkLabel(master=self.left_frame,
                                        text=("trans length average (Seconds)",
                                              goDelta.getSecondsFromRows(goDelta.getTranLengthAverage())))
        self.left_label5.grid(row=7,
                              column=0,
                              padx=(20, 10),
                              pady=(10, 10),
                              sticky="nsew")
        self.left_label6 = ctk.CTkLabel(master=self.left_frame,
                                        text=("BroadCast Length / Longest Recorded Burst (Seconds):",
                                              goDelta.getSecondsFromRows(goDelta.getTranLengthBroadcast())))
        self.left_label6.grid(row=8,
                              column=0,
                              padx=(20, 10),
                              pady=(10, 10),
                              sticky="nsew")

        self.left_label7 = ctk.CTkLabel(master=self.left_frame, text=(
        "Tranmission/Noise Difference %:", goDelta.getTranmissionNoiseDifference()))
        self.left_label7.grid(row=9,
                              column=0,
                              padx=(20, 10),
                              pady=(10, 10),
                              sticky="nsew")

        self.left_scrollBox = ScrollingFrameSean(master=self.left_frame, orientation="vertical", width=100, height=10,
                                                 corner_radius=0, label_text='EdgeList')
        self.left_scrollBox.addTextArray(goDelta.getGlobalEdgeList())
        self.left_scrollBox.grid(row=10,
                                 column=0,
                                 padx=(20, 10),
                                 pady=(10, 10),
                                 rowspan=1,
                                 sticky="new")
        # self.left_scrollBox.grid_propagate(0)

        self.left_label6 = ctk.CTkLabel(master=self.left_frame,
                                        text=("BroadCast Length / Longest Recorded Burst (Seconds):",
                                              goDelta.getSecondsFromRows(goDelta.getTranLengthBroadcast())))
        self.left_label6.grid(row=8,
                              column=0,
                              padx=(20, 10),
                              pady=(10, 10),
                              sticky="nsew")

        self.left_label7 = ctk.CTkLabel(master=self.left_frame, text=(
            "Tranmission/Noise Difference %:", goDelta.getTranmissionNoiseDifference()))
        self.left_label7.grid(row=9,
                              column=0,
                              padx=(20, 10),
                              pady=(10, 10),
                              sticky="nsew")
        self.left_scrollBox = ScrollingFrameSean(master=self.left_frame, orientation="vertical", width=100, height=10,
                                                 corner_radius=0, label_text='EdgeList')
        self.left_scrollBox.addTextArray(goDelta.getGlobalEdgeList())
        self.left_scrollBox.grid(row=10,
                                 column=0,
                                 padx=(20, 10),
                                 pady=(10, 10),
                                 rowspan=1,
                                 sticky="new")

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
                                            command=lambda: self.changeAlgo(CSVAlgoCopyPath),
                                            text_color=("gray10", "#DCE4EE"))
        self.default_button.grid(row=0,
                                 column=0,
                                 padx=(5, 5),
                                 pady=(20, 20), sticky="nsew")

        self.edit_button = ctk.CTkButton(master=self.sidebar_frame,
                                         text="Edit",
                                         command=self.openUserAlgoEdit,
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
                                         command=lambda: self.changeAlgo(userAlgoPath),
                                         text_color=("gray10", "#DCE4EE"))
        self.load_button.grid(row=3,
                              column=0,
                              padx=(5, 5),
                              pady=(20, 20), sticky="nsew")
        # this is to exit the screen
        self.exit_button = ctk.CTkButton(master=self,
                                         text="Exit",
                                         command=self.changeAlgo(userAlgoPath),
                                         text_color=("gray10", "#DCE4EE"))
        self.exit_button.grid(row=3,
                              column=4,
                              padx=(5, 5),
                              pady=(20, 20))
        self.defaultTrace(csvPath)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def defaultTrace(self, csvPath):
        print("default button")
        global canvas
        spectrogram = complex.readArrayAsMatrix(csvPath)

        # print(spectrogram)

        # plot.imshow(spectrogram, aspect='auto')
        # plot.xlabel("Frequency [MHz]")
        # plot.ylabel("Time [s]")
        fig, ax = plot.subplots(figsize=(4, 4))
        ax.set(xlabel='Frequency [MHz]', ylabel='Time [s]')

        ax.imshow(spectrogram, aspect='auto')
        fig.subplots_adjust()
        canvas = FigureCanvasTkAgg(fig, master=self.mid_frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.15, rely=0.15)
        # plot.show()

    def changeAlgo(self, algoPath):
        global csvPathTest
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = loadNewAnalytics.loadNewAnalytics(self, algoPath,
                                                                     csvPathTest)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def openUserAlgoEdit(self):
        from subprocess import call
        global userAlgoPath
        currentCall = "notepad "
        currentCall += userAlgoPath
        # startfile(userAlgoPath)
        call(currentCall)
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
        '''
        if(other > sliderLastNumber):
            self.plotZoom(1)
        else:
            self.plotZoom(-1)
        '''
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