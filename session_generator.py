from all_import import *

class Application:
    def __init__(self, master):

        self.master = master
        master.title("SSH Session Generator")
        master.protocol("WM_DELETE_WINDOW", self.store_session)
        master.resizable(False, False)

        self.hostConnectionConfig = Tkinter.LabelFrame(master, text=" 1. Enter Host Details: ")
        self.hostConnectionConfig.grid(row=0, columnspan=8, sticky='W', \
                                  padx=5, pady=5, ipadx=5, ipady=5)

        self.helpFrame = Tkinter.LabelFrame(master, text=" Instruction ")
        self.helpFrame.grid(row=0, column=9, columnspan=2, rowspan=7, \
                       sticky='NS', padx=5, pady=5)
        self.helpLabel = Tkinter.Label(self.helpFrame,
                                  text="This is simple ssh session generator. Just enter host IP, port and credentials. Add commands to execute if needed, number of sessions and click start. You will be informed when all sessions finish.",
                                  wraplength=200, anchor="e")
        self.helpLabel.grid(row=0)

        self.commandsConfig = Tkinter.LabelFrame(master, text=" 2. Enter Commands: ")
        self.commandsConfig.grid(row=2, columnspan=8, sticky='W', \
                            padx=5, pady=5, ipadx=5, ipady=5)

        self.sessionsConfig = Tkinter.LabelFrame(master, text=" 3. Configure Sessions: ")
        self.sessionsConfig.grid(row=3, columnspan=9, sticky='W', \
                            padx=5, pady=5, ipadx=5, ipady=5)

        self.hostLabel = Tkinter.Label(self.hostConnectionConfig, text="Host IP:")
        self.hostLabel.grid(row=0, column=0, sticky='E', padx=5, pady=2)

        self.hostEntry = Tkinter.Entry(self.hostConnectionConfig)
        self.hostEntry.grid(row=0, column=1, sticky="WE", pady=3)

        self.portLabel = Tkinter.Label(self.hostConnectionConfig, text="Port:")
        self.portLabel.grid(row=0, column=5, sticky='E', padx=5, pady=2)

        self.portEntry = Tkinter.Entry(self.hostConnectionConfig)
        self.portEntry.grid(row=0, column=7, sticky="WE", pady=2)
        self.portEntry.insert(0, '22')

        self.userLabel = Tkinter.Label(self.hostConnectionConfig, text="Username:")
        self.userLabel.grid(row=2, column=0, sticky='E', padx=5, pady=2)

        self.userEntry = Tkinter.Entry(self.hostConnectionConfig)
        self.userEntry.grid(row=2, column=1, sticky='E', pady=2)

        self.passLabel = Tkinter.Label(self.hostConnectionConfig, text="Password:")
        self.passLabel.grid(row=2, column=5, padx=5, pady=2)

        self.passEntry = Tkinter.Entry(self.hostConnectionConfig, show="*")
        self.passEntry.grid(row=2, column=7, pady=2)

        self.commandsLabel = Tkinter.Label(self.commandsConfig, \
                                      text="Enter the commands to execute in the one sessions (separate each command by &&)")
        self.commandsLabel.grid(row=4, column=0, padx=5, pady=2, sticky='W')

        self.commandsEntry = Tkinter.Entry(self.commandsConfig)
        self.commandsEntry.grid(row=5, columnspan=8, padx=5, pady=2, sticky='WE')

        self.checkboxVar = Tkinter.IntVar()
        self.sessionsCheckEntry = Tkinter.Checkbutton(self.sessionsConfig, \
                                                 text="Multiple sessions", onvalue=1, offvalue=0, variable=self.checkboxVar,
                                                 command=self.session_number_lock)
        self.sessionsCheckEntry.grid(row=6, sticky='W', padx=5, pady=2)

        self.sessionsNumberLabel = Tkinter.Label(self.sessionsConfig, \
                                            text="Specify number of sessions to generate:")
        self.sessionsNumberLabel.grid(row=6, column=2, columnspan=2, \
                                 sticky='W', padx=5, pady=2)

        self.sessionNumberEntry = Tkinter.Entry(self.sessionsConfig, state='disabled')
        self.sessionNumberEntry.grid(row=6, column=4, sticky='WE')

        # self.sessionsProgressBar = ttk.Progressbar(orient="horizontal", length=400, mode="determinate", maximum=100)
        # self.sessionsProgressBar.grid(row=7, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        # self.sessionsProgressBar["value"] = 0

        self.versionBox = Tkinter.LabelFrame(master, width=400, height=25, relief="flat")
        self.versionBox.grid(row=7, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        self.versionNumber = Tkinter.Label(self.versionBox, text="SSH Session Generator. Version 1.0. Copyright by Piotr Semeniuk.")
        self.versionNumber.grid(row=6, column=2, columnspan=2, sticky='WENS', padx=5, pady=2)

        self.startButton = Tkinter.Button(text="Start", command=self.generate_session)
        self.startButton.grid(row=7, column=2, sticky='W', \
                         padx=5, pady=5, ipadx=5, ipady=5)

        self.resetButton = Tkinter.Button(text="Clear", command=self.clear_entries)
        self.resetButton.grid(row=7, column=3, sticky='W', \
                         padx=5, pady=5, ipadx=5, ipady=5)

        self.restoreSessionButton = Tkinter.Button(text="Restore previous session config", command=self.restore_session)
        self.restoreSessionButton.grid(row=7, column=9, sticky='W', \
                                  padx=5, pady=5, ipadx=5, ipady=5)

        # Default values

        self.hostEntry.insert(0, '1.1.1.1')
        self.userEntry.insert(0, 'username')
        self.passEntry.insert(0, 'password')
        self.commandsEntry.insert(0, "command && command")

        self.create_dir()

    def clear_entries(self):
        self.hostEntry.delete(0, 'end')
        self.portEntry.delete(0, 'end')
        self.userEntry.delete(0, 'end')
        self.passEntry.delete(0, 'end')
        self.commandsEntry.delete(0, 'end')
        self.sessionsCheckEntry.deselect()
        self.sessionNumberEntry.delete(0, 'end')
        #self.sessionsProgressBar["value"] = 0

    def generate_session(self):
        portInt = int(self.portEntry.get())
        #self.sessionsProgressBar["value"] = 0

        if self.checkboxVar.get() == 0:
            start = time.time()
            connection = ssh_script.Ssh(self.hostEntry.get(), portInt, self.userEntry.get(), self.passEntry.get())
            connection.sendCommand(self.commandsEntry.get())
            end = time.time()
            final_time = (end - start)
            exec_time = str(round(final_time, 2))
            #self.sessionsProgressBar["value"] = 100

            showinfo("Information", "Session was generated successfully in " + exec_time + "s.")


        elif self.sessionNumberEntry.index("end") == 0:
            showerror("Error", "Field with the session number cannot be empty!")
        else:
            start = time.time()
            sessionNumber = int(self.sessionNumberEntry.get())
            progressValueIncrease = int(100 / sessionNumber)
            print progressValueIncrease

            for x in range(sessionNumber):
                connection = ssh_script.Ssh(self.hostEntry.get(), portInt, self.userEntry.get(), self.passEntry.get())
                connection.sendCommand(self.commandsEntry.get())
                #self.sessionsProgressBar["value"] += progressValueIncrease
            end = time.time()
            final_time = (end - start)
            exec_time = str(round(final_time, 2))
            #self.sessionsProgressBar["value"] = 100
            showinfo("Information", str(sessionNumber) + " sessions were generated sucessfully in " + exec_time + "s.")

    def session_number_lock(self):
        if self.checkboxVar.get() == 0:
            self.sessionNumberEntry.configure(state='disabled')
        else:
            self.sessionNumberEntry.configure(state='normal')

    def store_session(self):
        store = open("sessionData/last_session.txt", "w")
        store.write(self.hostEntry.get() + '\n')
        store.write(self.portEntry.get() + '\n')
        store.write(self.userEntry.get() + '\n')
        store.write(self.passEntry.get() + '\n')
        store.write(self.commandsEntry.get() + '\n')
        store.close()
        self.master.quit()

    def restore_session(self):
        backup = open("sessionData/last_session.txt", "r")
        self.hostEntry.insert(0, backup.readline())
        self.portEntry.insert(0, backup.readline())
        self.userEntry.insert(0, backup.readline())
        self.passEntry.insert(0, backup.readline())
        self.commandsEntry.insert(0, backup.readline())
        backup.close()

    def create_dir(self):
        dir_name = 'sessionData'

        try:
            os.mkdir(dir_name)
        except OSError as e:
            if e.errno == errno.EEXIST:
                print "Directory not created as it already exist."
            else:
                raise




root = Tkinter.Tk()
my_gui = Application(root)
root.mainloop()