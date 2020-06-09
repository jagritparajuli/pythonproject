from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import PyPDF2

class Application(Tk):
    def __init__(self):
        super(Application,self).__init__()
        self.title('Hmm PDF')
        self.minsize(600,400)

        self.tab = ttk.Notebook(self)
        self.rotate()
        self.merge()
        self.tab.pack(expan=1,fill = "both")

    
    def rotate(self):
        tab_rotate = ttk.Frame(self.tab)
        self.tab.add(tab_rotate,text="Rotate")

         # getting file
        self.file_label = ttk.LabelFrame(tab_rotate, text = "Select the pdf to rotate")
        self.file_label.grid(column = 0, row = 0, pady=50, padx = 20, sticky = "W")
        self.file_button()

        # getting angle
        self.angle_frame = ttk.LabelFrame(tab_rotate, text = "Angle")
        self.angle_frame.grid(row = 2, column = 0, sticky = "W", padx=20)
        self.angle_value = ttk.Entry(self.angle_frame)
        self.angle_value.grid(row = 3 , column = 0)
        self.angle_button()

        #output file
        self.output_frame = ttk.LabelFrame(tab_rotate, text = "Rotate and Save")
        self.output_frame.grid(column = 0, row = 5,pady=20, padx = 20, sticky = "W")
        self.output_button_rotate()


    def merge(self):
        tab_merge = ttk.Frame(self.tab)
        self.tab.add(tab_merge,text="Merge")
         # getting file
        self.files_label = ttk.LabelFrame(tab_merge, text = "Select the PDF files to merge")
        self.files_label.grid(column = 0, row = 0, pady=50, padx = 20, sticky = "W")
        self.files_button()

        self.output_frame_merge = ttk.LabelFrame(tab_merge, text = "Merge and Save")
        self.output_frame_merge.grid(column = 0, row = 3,pady=20, padx = 20, sticky = "W")
        self.output_button_merge()


    def file_button(self):
        self.button = ttk.Button(self.file_label, text = 'Browse', command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def files_button(self):
        self.button_files = ttk.Button(self.files_label, text = 'Browse', command = self.filesDialog)
        self.button_files.grid(column = 1, row = 1)

    def fileDialog(self):
        self.file_name = filedialog.askopenfilename(initialdir = "/Projects\Python\pdf\pdfs", title = 'Select a file', filetypes = (('PDF files','*.pdf'),('All Files','*.*')))
        self.file_label = ttk.Label(self.file_label, text =self.file_name)
        self.file_label.grid(column = 2 , row = 1)
    
    def filesDialog(self):
        self.file_names = filedialog.askopenfilenames(initialdir = "/Projects\Python\pdf\pdfs", title = 'Select a file', filetypes = (('PDF files','*.pdf'),('All Files','*.*')))
        self.files_label = ttk.Label(self.files_label, text =self.file_names)
        self.files_label.grid(column = 2 , row = 1)

    def angle_button(self):
        self.button1 = ttk.Button(self.angle_frame, text = "Set",command = self.get_angle)
        self.button1.grid(column = 1, row = 3)

    def get_angle(self):
        self.angle = int(self.angle_value.get())
        self.angle_label = ttk.Label(self.angle_frame, text ="Rotate By: "+str(self.angle)+ " degrees")
        self.angle_label.grid(column = 1 , row = 4)

    def output_button_rotate(self):
        self.button2 = ttk.Button(self.output_frame, text = 'Rotate and save', command = self.outputDialog_rotate)
        self.button2.grid(row = 6, column = 1)
    
    def output_button_merge(self):
        self.button2 = ttk.Button(self.output_frame_merge, text = 'Merge and save', command = self.outputDialog_merge)
        self.button2.grid(row = 3, column = 1)

    def outputDialog_rotate(self):
        self.output_file = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=(('PDF','*.pdf'),('All files','*.*')))
        self.output_file_label = ttk.Label(self.output_frame,text = "File Saved")
        self.output_file_label.grid(column = 3, row = 6)
        self.rotate_file()


    def outputDialog_merge(self):
        self.output_file = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=(('PDF','*.pdf'),('All files','*.*')))
        self.output_file_label = ttk.Label(self.output_frame_merge,text = "File Saved")
        self.output_file_label.grid(column = 3, row = 6)
        self.merge_file()
    
    def rotate_file(self):
        file = open(self.file_name,'rb')
        self.pdf_reader = PyPDF2.PdfFileReader(file)
        self.pdf_writer = PyPDF2.PdfFileWriter()
        for page in range(self.pdf_reader.numPages):
            page_obj = self.pdf_reader.getPage(page)
            page_obj.rotateClockwise(self.angle)
            self.pdf_writer.addPage(page_obj)
        output = open(self.output_file,'wb')
        self.pdf_writer.write(output)
        output.close()


    def merge_file(self):
        self.pdf_writer = PyPDF2.PdfFileWriter()
        for path in self.file_names:
            self.pdf_reader = PyPDF2.PdfFileReader(path)
            for page in range(self.pdf_reader.getNumPages()):
                self.pdf_writer.addPage(self.pdf_reader.getPage(page))
        with open(self.output_file, 'wb') as out:
            self.pdf_writer.write(out)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
