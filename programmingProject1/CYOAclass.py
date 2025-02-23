from tkinter import filedialog, ttk
import tkinter.font as tkFont

class CYOA:     
    def __init__(self, root):   
        
        # Theme:
        # https://github.com/rdbende/Azure-ttk-theme
        root.tk.call('source', 'Azure/azure.tcl')
        root.tk.call('set_theme', 'dark')
        
        # styles:
        self.s = ttk.Style()
        self.headerFont = tkFont.Font(size=18, weight="bold", family="Times")
        self.bodyFont = tkFont.Font(size=16, weight="normal", family="Times")
        # self.btnFont = tkFont.Font(size=14, weight="normal")
        #styling the button, this had to go after the implimentation of the theme
        self.s.configure('TButton', font=('Times', 14))
        
        
        # set the size of the window
        root.geometry("800x400")
        # set the window title
        root.title("Choose Your Own Adventure!")
        # label for the page title
        self.title = ttk.Label(root, font=self.headerFont)
        self.title.pack(pady=10)

        # frame for the story
        self.storyFrame = ttk.Frame(root)
        # add columns to the frame, there are two columns of equal weight
        self.storyFrame.columnconfigure(0, weight=2)
        self.storyFrame.columnconfigure(1, weight=2)
        # create 2 labels to hold 2 potential paragraphs
        self.storyIntro = ttk.Label(self.storyFrame, wraplength=500, font=self.bodyFont, justify="left")
        self.story = ttk.Label(self.storyFrame, wraplength=500, font=self.bodyFont, justify="left")
        # put the story in the columns, starting in column 0 and spanning both columns so that it's centered
        self.storyIntro.grid(row=0, column=0, columnspan=2, sticky='wens',padx=70, pady=5)
        self.story.grid(row=1, column=0, columnspan=2, sticky='wens',padx=70, pady=20)

        self.storyFrame.pack()
        

        # make a button frame, similarly to the story from
        self.buttonFrame = ttk.Frame(root)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        
        self.btn = ttk.Button(self.buttonFrame, padding=10, style='TButton')
        self.btn.grid(row=0, column=0, columnspan=2, sticky="wens", padx=20)
        
        self.btn1 = ttk.Button(self.buttonFrame, padding=15, style='TButton')
        self.btn1.grid(row=0, column=0, sticky='wens', padx=20)
        
        self.btn2 = ttk.Button(self.buttonFrame, padding=15, style='TButton')
        self.btn2.grid(row=0, column=1, sticky='wens', padx=20)
        
        self.buttonFrame.pack()
        
        
        # a variable to hold the path where we will write out the story 
        self.path = "";
        

    def oneButtonGrid(self):
        self.btn1.grid_forget()
        self.btn2.grid_forget()
        self.btn.grid(row=0, column=0, columnspan=2, sticky="wens", padx=20)
        
    def twoButtonsGrid(self):
        self.btn.grid_forget()
        self.btn1.grid(row=0, column=0, sticky='wens', padx=20)
        self.btn2.grid(row=0, column=1, sticky='wens', padx=20)
        

    # fucntion that creates a page with 2 button options
    def newQuestionPage(self, titleText, storyText, option1, option2, function1, function2, storyIntroText="", write=False):
        self.title.config(text=titleText)
        #I had to do this to that previous single buttons wouldn't show up
        if storyIntroText != "":
            self.storyIntro.config(text=storyIntroText)
        else:
            self.storyIntro.config(text="")
        self.story.config(text=storyText)
        
        #set the grid to 2 buttons
        self.twoButtonsGrid()
      
        #configure the buttons
        self.btn1.config(text=option1, command=lambda:function1())
        self.btn2.config(text=option2, command=lambda:function2())
        
        if write:
            if storyIntroText:
                self.write(storyIntroText)
            self.write(storyText)
        
    #function that creates a page with one button option
    def newContinuePage(self, titleText, storyText, buttonText, function, storyIntroText = "", write=False):

        self.title.config(text=titleText)
        if storyIntroText != "":
            self.storyIntro.config(text=storyIntroText)
        else:
            self.storyIntro.config(text="")
        self.story.config(text=storyText)
  
        # self.prepButtonFrame(1)
        self.oneButtonGrid()
        self.btn.config(text=buttonText, command=lambda:function())
        
        if write:
            if storyIntroText:
                self.write(storyIntroText)
            self.write(storyText)
        
    def open_file_dialog(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        self.path = file_path
        return file_path


    def write(self, storyString):
        if self.path != "":
            try:
                with open(self.path, 'a') as file:
                    file.write(f"{storyString}\n")
            except FileNotFoundError:
                    print("ERROR")
                    
                    
                    
                    
